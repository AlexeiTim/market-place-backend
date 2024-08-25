from rest_framework.routers import DefaultRouter
from blog import views

app_name = 'blog'

router = DefaultRouter()
router.register('posts', views.PostViewSet, basename='posts')
urlpatterns = []

urlpatterns += router.urls