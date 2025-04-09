from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Import your custom user model

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser  # Use your custom user model
        fields = ("username", "email", "role")  # Add fields you want
