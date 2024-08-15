from rest_framework.routers import DefaultRouter
from products import views

app_name = 'products'

router = DefaultRouter()
router.register('products', views.ProductListViewSet, basename='products')
urlpatterns = []

urlpatterns += router.urls
