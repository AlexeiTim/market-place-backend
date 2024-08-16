from django.shortcuts import render, get_object_or_404
from cart import serializers, models
from rest_framework import viewsets, views, status
from rest_framework.response import Response
from products.models import Product
# Create your views here.


class CartViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Cart.objects.all()
    serializer_class = serializers.CartSerializer

    def get_queryset(self):
        return models.Cart.objects.all()[:1]


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = models.CartItem.objects.all()
    serializer_class = serializers.CartItemSerializer
    pagination_class = None

    def perform_create(self, serializer):
        cart = models.Cart.objects.first()
        serializer.save(cart=cart)

    def partial_update(self, request, *args, **kwargs):
        cart_item = self.get_object()
        quantity = request.data.get('quantity')
        cart_item.quantity += quantity
        if cart_item.quantity < 1:
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        cart_item.save()
        return Response(serializers.CartItemSerializer(cart_item).data)


class AddToCartView(views.APIView):
    def post(self, request):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        if not product_id:
            Response({"error": "Product ID is required"})

        try:
            print(product_id)
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"})

        cart, created = models.Cart.objects.get_or_create(id=1)

        cart_item, created = models.CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()

        serializer = serializers.CartItemSerializer(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RemoveFromCartView(views.APIView):
    def delete(self,request):
        product_id = request.data.get('product_id')

        if not product_id:
            return Response({ "error": "Product Id is required"})

        cart = get_object_or_404(models.Cart, id=1)
        cart_item = get_object_or_404(models.CartItem, cart=cart, product_id=product_id)
        cart_item.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)