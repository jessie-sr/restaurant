from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant
from .serializers import RestaurantSerializer

# Implement a view that lists all restaurants.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

