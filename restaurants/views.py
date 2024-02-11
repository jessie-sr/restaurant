from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Restaurant

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/list.html'  # Path to your template
    context_object_name = 'restaurants'

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurants/detail.html'  # Path to your detail template
    context_object_name = 'restaurant'
