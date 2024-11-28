# file_sharing/urls.py
from django.contrib import admin
from django.urls import path, include  # Make sure `include` is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include api.urls here
]
