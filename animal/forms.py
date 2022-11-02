from dataclasses import fields
from django import forms
from .models import Animal
from django.core.exceptions import ValidationError

def validate_even(value):
    if not(value >0):
        raise ValidationError(
            _('%(value)s No es un número válido'),
            params={'value': value},
        )

        
class FormularioAnimals(forms.ModelForm):


    age = forms.IntegerField(label='Edad', initial=0, required=True,
    validators=[validate_even],
                             widget=forms.NumberInput(attrs={'class': 'form-control','required':'True'}))
    description = forms.CharField(label='Descripcion', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))

    picture = forms.ImageField(label='Subir foto', required=True,widget=forms.FileInput(attrs={'required':'True', 'help_text':'Campo requerido'}))

    
    class Meta:
        model = Animal
        fields = ['age', 'description', 'picture']
