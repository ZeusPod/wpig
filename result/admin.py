from django.contrib import admin
from .models import Resultados
# Register your models here.


class ResultadosAdmin(admin.ModelAdmin):
    list_display = (
        'animal_id','name_foto','resultado', 'sintomas','recomendaciones', 'result_date'
    )
    ordering=('result_date',)


admin.site.register(Resultados, ResultadosAdmin)