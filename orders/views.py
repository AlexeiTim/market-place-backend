from django.shortcuts import render
from rest_framework import viewsets
from orders import models, serializers
from cart.models import Cart, CartItem
from django.core.exceptions import PermissionDenied


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
        serializer.save(user=self.request.user)

        # Получение корзины пользователя и удаление всех её элементов
        cart = Cart.objects.filter(user=self.request.user).first()
        if cart:
            CartItem.objects.filter(cart=cart).delete()