from django.db import models

# Create your models here.
class Sintomas(models.Model):
    tipos = models.PositiveIntegerField()
    name = models.CharField('neumonia' ,null=True, max_length=255)
    sintomas = models.TextField()
    

    def __str__(self) -> str:
        return self.sintomas

    class Meta:
        verbose_name = 'Sintoma' 
        verbose_name_plural = 'Sintomas'

