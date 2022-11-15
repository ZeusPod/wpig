
from django.contrib import admin
from .models import Recomendaciones
# Register your models here.


class RecomendacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipos','name','recomendaciones')
    ordering = ('id',)


admin.site.register(Recomendaciones, RecomendacionesAdmin)