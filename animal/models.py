from distutils.command.upload import upload
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


class Animal(models.Model):
    age = models.PositiveIntegerField(max_length=20)
    date = models.DateField()    
    picture = models.ImageField(upload_to='animal/', null=True, blank=True)
    # user relationship
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.user_id.username


    class Meta:
        verbose_name = 'Animal' 
        verbose_name_plural = 'Animals' 