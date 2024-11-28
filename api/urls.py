# file_sharing/api/urls.py
from django.urls import path
from .views import SignupView  # Make sure you import your views here

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),  # This defines the signup endpoint
    # Add other API endpoints as required
]
