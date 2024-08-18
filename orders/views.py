from rest_framework import viewsets
from orders import models, serializers
from cart.models import Cart, CartItem
from django.core.exceptions import PermissionDenied
from wallet.models import Wallet


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    pagination_class = None

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return models.Order.objects.filter(user=self.request.user)
        return models.Order.objects.none()

    def perform_create(self, serializer):
        if not self.request.user.is_authenticated:
            raise PermissionDenied("User must be authenticated to create an order.")
        order = serializer.save(user=self.request.user)
        wallet = Wallet.objects.filter(user=self.request.user).first()
        wallet.cash = wallet.cash - order.total_price
        wallet.save()

        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            CartItem.objects.filter(cart=cart).delete()

    def perform_destroy(self, instance):
        wallet = Wallet.objects.filter(user=self.request.user).first()
        order_total_price = instance.total_price
        wallet.cash += order_total_price
        wallet.save()
        instance.delete()
