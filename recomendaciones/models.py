from django.db import models


# Create your models here.
class Recomendaciones(models.Model):
    tipos = models.PositiveBigIntegerField()
    name = models.CharField('neuominia', null=True, max_length=255)
    recomendaciones = models.TextField()


    def __str__(self) -> str:
        return self.recomendaciones


    class Meta:
        verbose_name = 'Recomendacion'
        verbose_name_plural = 'Recomendaciones'