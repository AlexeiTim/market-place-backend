from rest_framework.routers import DefaultRouter
from orders import views

app_name = 'orders'

router = DefaultRouter()
router.register('orders', views.OrderViewSet, basename='orders')

urlpatterns = []

urlpatterns += router.urls
