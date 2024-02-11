from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet

# Set up app-level URL configuration.
router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]