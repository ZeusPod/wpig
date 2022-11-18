from django.contrib import admin
from .models import Animal
# Register your models here.

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'age', 'description', 'picture', 'establo', 'galpon', 'born_date', 'place_of_birth')
    ordering = ('user_id',)
    search_fields = ('user_id', 'age')

admin.site.register(Animal, AnimalAdmin)