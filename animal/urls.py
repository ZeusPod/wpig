from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.create_animal, name='create_animal'),
    path('all_animals/', views.get_all_animals, name='get_animals'),
    path('delete_animals/<int:animal_id>', views.delete_animals, name='delete_animals')
]