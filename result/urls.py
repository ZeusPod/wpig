from django.urls import path
from . import views


urlpatterns = [
    path('process_image/<int:animal_id>', views.process_image, name='process_image'),
]