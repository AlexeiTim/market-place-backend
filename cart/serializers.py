from rest_framework import serializers
from cart import models
from products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    class Meta:
        model = models.CartItem
        fields = '__all__'
