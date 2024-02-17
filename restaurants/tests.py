from django.test import TestCase
from django.urls import reverse
from .models import Restaurant
from django.contrib.auth.models import User

# Test Case 1: Viewing a List of All Restaurants
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

# Test Case 2: Retrieving Detailed Information About a Specific Restaurant
class RestaurantDetailViewTests(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(name='Test Restaurant', location='Test Location', cuisine='Test Cuisine', rating=4.0)

    def test_view_detail(self):
        response = self.client.get(reverse('restaurant-detail', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.restaurant.name)

# Test Case 3: Adding a New Restaurant
class RestaurantCreateViewTests(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='12345')
    
    def test_create_restaurant(self):
        # Log in the test user
        self.client.login(username='testuser', password='12345')
        
        response = self.client.post(reverse('add_restaurant'), {
            'name': 'New Restaurant', 
            'location': 'New Location', 
            'cuisine': 'New Cuisine', 
            'rating': 4.0,
            'phone': 123-456-789,
            'email': 'info@newrestaurant.com'
        })
        
        self.assertEqual(response.status_code, 302)  # Assuming redirect after creation
        self.assertEqual(Restaurant.objects.last().name, 'New Restaurant')

# Test Case 4: Updating an Existing Restaurant
class RestaurantUpdateViewTests(TestCase):
    def setUp(self):
        # Create a test user and a test restaurant
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.restaurant = Restaurant.objects.create(
            name='Old Restaurant', 
            location='Old Location', 
            cuisine='Old Cuisine', 
            rating=3.5,
            phone=123-456-789,
            email='info@oldrestaurant.com'
        )

    def test_update_restaurant(self):
        # Log in the test user
        self.client.login(username='testuser', password='12345')
        
        self.client.post(reverse('restaurant-update', args=[self.restaurant.id]), {
            'name': 'Updated Restaurant', 
            'location': 'Updated Location', 
            'cuisine': 'Updated Cuisine', 
            'rating': 4.5,
            'phone': 123-456-789,
            'email': 'info@newrestaurant.com'
        })
        
        self.restaurant.refresh_from_db()
        self.assertEqual(self.restaurant.name, 'Updated Restaurant')

