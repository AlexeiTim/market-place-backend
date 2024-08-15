import django_filters as filters
from products import models


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    rating = filters.NumberFilter(field_name='rating')
    category = filters.CharFilter(field_name='category__name')
    brand = filters.CharFilter(field_name='brand__name')
    ordering = filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('rating', 'rating'),
            ('name', 'name')
        )
    )
    search = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = models.Product
        fields = ['min_price', 'max_price', 'rating', 'category', 'brand', 'ordering', 'search']
