from django import forms
from .models import Restaurant
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'location', 'cuisine', 'rating', 'phone', 'email']

class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)