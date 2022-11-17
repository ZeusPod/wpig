from django.urls import path
from . import views


urlpatterns = [
    path('process_image/<int:animal_id>', views.process_image, name='process_image'),
    path('get_results/', views.get_results , name='get_results')
]