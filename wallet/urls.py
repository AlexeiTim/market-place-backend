from rest_framework.routers import DefaultRouter
from wallet import views

app_name = 'wallet'

router = DefaultRouter()
router.register('wallets', views.WalletViewSet, basename='wallets')

urlpatterns = [

]

urlpatterns += router.urls
