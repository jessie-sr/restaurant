from django.views.generic import ListView
from django.views.generic import DetailView
from django.shortcuts import render, redirect
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

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurants:list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/add.html', {'form': form})