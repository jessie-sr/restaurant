from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from ..models import Restaurant
from ..forms import RestaurantForm

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant/list.html'
    context_object_name = 'restaurants'

    # Filter the queryset based on the location and cuisine
    def get_queryset(self):
        queryset = super().get_queryset()
        location = self.request.GET.get('location')
        cuisine = self.request.GET.get('cuisine')

        if location:
            queryset = queryset.filter(location__icontains=location)
        if cuisine:
            queryset = queryset.filter(cuisine__icontains=cuisine)

        return queryset

    #  Add these lists to the context so they can be accessed in the template
    def get_context_data(self, **kwargs):
        context = super(RestaurantListView, self).get_context_data(**kwargs)
        context['locations'] = Restaurant.objects.order_by('location').values_list('location', flat=True).distinct()
        context['cuisines'] = Restaurant.objects.order_by('cuisine').values_list('cuisine', flat=True).distinct()
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant/detail.html'
    context_object_name = 'restaurant'

class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant/add.html'
    success_url = reverse_lazy('restaurant-list')  # Redirect to the restaurant list after creation

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurant/delete.html'
    success_url = reverse_lazy('restaurant-list')  # Redirect to the restaurant list after deletion
    context_object_name = 'restaurant'

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant/update.html'
    success_url = reverse_lazy('restaurant-list')