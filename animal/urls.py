from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.create_animal, name='create_animal')
]