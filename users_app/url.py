from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users_app.views import (RegisterViewset,LoginViewSet,
                             InventViewset,UserProfileViewSet)


router = DefaultRouter(trailing_slash = False)
router.register(r'register',RegisterViewset, basename='user')
router.register(r'login',LoginViewSet, basename='user')
router.register(r'add-invention',InventViewset, basename='invention')
router.register(r'user-profile',UserProfileViewSet, basename='user-profile')

urlpatterns = [
    url(r'',include(router.urls))
]
