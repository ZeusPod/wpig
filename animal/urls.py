from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.create_animal, name='create_animal'),
    path('all_animals/', views.get_all_animals, name='get_animals')
]