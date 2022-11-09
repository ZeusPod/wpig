from django.contrib import admin
from .models import Sintomas
# Register your models here.


class SintomasAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipos','name','sintomas')
    ordering = ('id',)


admin.site.register(Sintomas, SintomasAdmin)