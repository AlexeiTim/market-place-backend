from django.shortcuts import render
from rest_framework import viewsets, generics
from products import models, serializers, filters
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
# Create your views here.


class ProductListViewSet(viewsets.ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filterset_class = filters.ProductFilter
    permission_classes = [AllowAny, ]


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = None
    permission_classes = [AllowAny, ]


class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
    pagination_class = None
    permission_classes = [AllowAny, ]


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    pagination_class = None
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        product_id = self.request.query_params.get('product_id')
        if product_id:
            return self.queryset.filter(product__id=product_id)
        return self.queryset
