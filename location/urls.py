from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('l/', views.create_location, name='location_view'),  # Changed to the root URL
    # Serve media files during development
   
]
