from django.shortcuts import render
from rest_framework import viewsets
from orders import models, serializers
from cart.models import Cart, CartItem


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    pagination_class = None

    def perform_create(self, serializer):
        serializer.save()
        CartItem.objects.filter(cart=1).delete()


