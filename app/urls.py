"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path, include
from app.views import home, consejos
from django.conf import settings
from django.conf.urls.static import static
from .views import SingUpView
from animal import urls
from result import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home' ),
    path('consejos/', consejos, name='consejos' ),
    path('accounts/', include('django.contrib.auth.urls')),
    path('singup/',SingUpView.as_view() , name='singup'),
    path('animal/', include('animal.urls')),
    path('result/', include('result.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)