from django.shortcuts import render
from rest_framework import viewsets
from products import models, serializers
# Create your views here.


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer