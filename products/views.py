from django.shortcuts import render
from rest_framework import viewsets, generics
from products import models, serializers, filters
# Create your views here.


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = None


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    pagination_class = None
