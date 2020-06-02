from django.conf.urls import url
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from network.views import ConnectionViewsets

router = DefaultRouter(trailing_slash=False)

router.register(r'initiate-connection', ConnectionViewsets, basename='connection')

urlpatterns = [
    url(r'',include(router.urls))
]