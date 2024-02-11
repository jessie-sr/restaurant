from django.urls import path
from .views import RestaurantListView, RestaurantDetailView, RestaurantCreateView, RestaurantDeleteView, RestaurantUpdateView
from . import views

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/add/', RestaurantCreateView.as_view(), name='add_restaurant'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),
    path('restaurant/update/<int:pk>/', RestaurantUpdateView.as_view(), name='restaurant-update'),
]
