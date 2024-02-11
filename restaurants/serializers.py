from rest_framework import serializers
from .models import Restaurant

# Define a serializer for the Restaurant model.
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'location', 'cuisine', 'rating', 'phone', 'email']
