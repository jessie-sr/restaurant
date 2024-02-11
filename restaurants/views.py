from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('restaurant-list')  # Redirect to the restaurant list after creation

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurants/delete.html'
    success_url = reverse_lazy('restaurant-list')  # Redirect to the restaurant list after deletion
    context_object_name = 'restaurant'

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurants/update.html'
    success_url = reverse_lazy('restaurant-list')