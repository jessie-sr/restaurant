from django.urls import path
from .views import RestaurantListView, RestaurantDetailView
from . import views

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/add/', views.add_restaurant, name='add_restaurant'),
]