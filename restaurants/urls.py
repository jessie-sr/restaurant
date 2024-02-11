from django.urls import path, include
from .views.restaurant import RestaurantListView, RestaurantDetailView, RestaurantCreateView, RestaurantDeleteView, RestaurantUpdateView
from django.contrib.auth import views as auth_views
from .views.user import SignUpView

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),
    path('restaurants/add/', RestaurantCreateView.as_view(), name='add_restaurant'),
    path('restaurant/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),
    path('restaurant/<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
