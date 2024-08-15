from rest_framework.routers import DefaultRouter
from products import views
from django.urls import path

app_name = 'products'

router = DefaultRouter()
router.register('products', views.ProductListViewSet, basename='products')
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('brands', views.BrandViewSet, basename='brands')
urlpatterns = [

]

urlpatterns += router.urls
