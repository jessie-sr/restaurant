from django.test import TestCase
from django.urls import reverse
from .models import Restaurant

class RestaurantListViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create test data
        number_of_restaurants = 5
        for restaurant_id in range(number_of_restaurants):
            Restaurant.objects.create(name=f'Restaurant {restaurant_id}', location='Location', cuisine='Cuisine', rating=4.5)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/api/restaurants/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('restaurant-list'))
        self.assertEqual(response.status_code, 200)

    def test_lists_all_restaurants(self):
        response = self.client.get(reverse('restaurant-list'))
        self.assertEqual(len(response.context['restaurants']), 5)
