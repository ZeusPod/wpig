from urllib import request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User

@login_required
def home(request):
    return render(request, 'index.html')



def login(request):
    return render(request, 'login.html')


""" def exit(request):
    if not request.user.is_authenticated:
        return redirect('login')
    logout(request)
    return redirect('login') """