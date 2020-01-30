from django.urls import path, include
from rest_framework import routers
from .views import DataView


router = routers.DefaultRouter()
router.register("data", DataView, basename="data")


urlpatterns = [
    path('', include(router.urls))
]
