from django.db import models
from animal.models import Animal

# Create your models here.
class Resultados(models.Model):
    animal_id = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    name_foto = models.CharField(max_length=255)
    establo = models.CharField(max_length=255)
    galpon = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    register_date = models.CharField(max_length=255)
    born_date = models.CharField(max_length=255)
    place_of_birth = models.CharField(max_length=255)
    resultado = models.CharField(max_length=255)
    sintomas = models.TextField()
    recomendaciones = models.TextField()
    result_date = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.resultado


    class Meta:
     verbose_name = 'Resultado'
     verbose_name_plural = 'Resultados'