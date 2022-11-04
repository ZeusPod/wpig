from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy


@login_required
def home(request):
    return render(request, 'index.html')



def login(request):
    return render(request, 'login.html')

def consejos(request):
    return render(request, 'consejos.html')


class SingUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/singup.html'