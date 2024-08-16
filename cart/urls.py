from rest_framework.routers import DefaultRouter
from cart import views
from django.urls import path

app_name = 'cart'

router = DefaultRouter()
router.register('carts', views.CartViewSet, basename='carts')
router.register('cart-items', views.CartItemViewSet, basename='cart-items')

urlpatterns = [
    path('add-to-cart/', views.AddToCartView.as_view(), name='add-to-cart'),
    path('remove-from-cart/', views.RemoveFromCartView.as_view(), name='remove-from-cart')
]

urlpatterns += router.urls