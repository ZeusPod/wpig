from django.db import models
from animal.models import Animal

# Create your models here.
class Resultados(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    name_foto = models.ImageField(null=False, upload_to="result/")
    resultado = models.CharField(max_length=255)
    sintomas = models.TextField()
    recomendaciones = models.TextField()
    result_date = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.resultado


    class Meta:
     verbose_name = 'Resultado'
     verbose_name_plural = 'Resultados'