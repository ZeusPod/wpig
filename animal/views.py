from email import message
from django.shortcuts import redirect, render
from animal.forms import FormularioAnimals
from django.contrib.auth.models import User
from .models import Animal
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def create_animal(request):
    if request.user.is_authenticated:
        form = FormularioAnimals(request.POST, request.FILES)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.user_id = request.user
            formulario.save()
            messages.success(request,'Cerdo agregado con exito')
            return redirect('home')
        context={
            'form':form,
        }
        
        return render(request, 'animal/register_animal.html', context)
    else:
        return render(request, 'animal/register_animal.html')
        
        
# get alls animals
def get_all_animals(request):
    if request.method == "GET":
        animals = Animal.objects.all()
        return render(request, 'animal/list_animals.html', {'animals':animals})


# delete animals 
def delete_animals(request,animal_id):
    animal = Animal.objects.get(pk=animal_id)
    animal.delete()
    animals = Animal.objects.all()
    messages.success(request, 'Solicitud eliminada con exito')
    return render(request, 'animal/list_animals.html', {'animals':animals})


# get animal by id
def get_animal_id(request, animal_id):
    data = Animal.objects.get(pk=animal_id)
    return render(request, 'detail/detail.html', {'data':data})