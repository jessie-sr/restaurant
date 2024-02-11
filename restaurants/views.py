from django.views.generic import ListView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Restaurant
from .forms import RestaurantForm

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurants/list.html'
    context_object_name = 'restaurants'

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurants/detail.html'
    context_object_name = 'restaurant'

class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurants/add.html'
    success_url = reverse_lazy('restaurant-list')