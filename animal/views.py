from email import message
from django.shortcuts import redirect, render
from animal.forms import FormularioAnimals
from django.contrib.auth.models import User
from .models import Animal


# Create your views here.
def create_animal(request):
    if request.user.is_authenticated:
        form = FormularioAnimals(request.POST, request.FILES)
        if form.is_valid():
            formulario = form.save(commit=False)
            formulario.user_id = request.user
            formulario.save()
            return redirect('home')
        context={
            'form':form,
        }
        
        return render(request, 'animal/register_animal.html', context)
    else:
        return render(request, 'animal/register_animal.html')
        
        
