from django.db import models
from animal.models import Animal
from sintomas.models import Sintomas

# Create your models here.
class Result(models.Model):
    animal_id = models.ForeignKey(Animal,on_delete=models.CASCADE )
    creation_date = models.DateField(auto_now_add=True)
    result = models.IntegerField()
    sintomas_id = models.ForeignKey(Sintomas, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.animal_id

    class Meta:
        verbose_name = 'Result' 
        verbose_name_plural = 'Results' 