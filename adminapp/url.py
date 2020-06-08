from django.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from adminapp.views import AdminLoginViewSet


router = DefaultRouter(trailing_slash=False)
router.register(r'login', AdminLoginViewSet, basename='admin-login')

urlpatterns = [
    url(r'admin/', include(router.urls)),
]
