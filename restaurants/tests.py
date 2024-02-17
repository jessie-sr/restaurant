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

# Test Case 5: Deleting a Restaurant
class RestaurantDeleteViewTests(TestCase):
    def setUp(self):
        self.user_password = 'mypassword'
        self.user = User.objects.create_user('testuser', 'user@example.com', self.user_password)
        self.restaurant = Restaurant.objects.create(name='Delete Restaurant', location='Delete Location', cuisine='Delete Cuisine', rating=2.5)

    def test_delete_restaurant_without_login(self):
        """
        Test that unauthenticated user cannot delete a restaurant and is redirected.
        """
        response = self.client.post(reverse('restaurant-delete', args=[self.restaurant.id]))
        self.assertNotEqual(response.status_code, 200)
        self.assertTrue(Restaurant.objects.filter(id=self.restaurant.id).exists())
        
    def test_delete_restaurant_with_login(self):
        """
        Test that an authenticated user can delete a restaurant.
        """
        self.client.login(username=self.user.username, password=self.user_password)
        response = self.client.post(reverse('restaurant-delete', args=[self.restaurant.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Restaurant.objects.filter(id=self.restaurant.id).exists())

# Test Case 6: Filtering Restaurants Based on Location or Cuisine
class RestaurantFilterViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Restaurant.objects.create(name='Italian in Rome', location='Rome', cuisine='Italian', rating=4.7)
        Restaurant.objects.create(name='Sushi in Tokyo', location='Tokyo', cuisine='Japanese', rating=4.9)

    def test_filter_by_location(self):
        response = self.client.get(reverse('restaurant-list') + '?location=Rome')
        self.assertEqual(len(response.context['restaurants']), 1)
        self.assertEqual(response.context['restaurants'][0].location, 'Rome')

    def test_filter_by_cuisine(self):
        response = self.client.get(reverse('restaurant-list') + '?cuisine=Japanese')
        self.assertEqual(len(response.context['restaurants']), 1)
        self.assertEqual(response.context['restaurants'][0].cuisine, 'Japanese')
