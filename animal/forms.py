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

    raza = forms.CharField(label='Raza', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    establo = forms.CharField(label='Establo', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    galpon = forms.CharField(label='Galpon', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))

    place_of_birth = forms.CharField(label='place_of_birth', required=True, max_length=255, widget=forms.TextInput(attrs={'class':'form-control'}))

    born_date = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Fecha de nacimiento', 'type':'date'}))
    



    class Meta:
        model = Animal
        fields = ['age', 'description', 'picture', 'raza', 'establo', 'galpon', 'place_of_birth', 'born_date']
