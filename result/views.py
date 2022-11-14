from django.shortcuts import render
from animal.models import Animal
from utils.neuronal import predict


# Process image
def process_image(request,animal_id):
    animal = Animal.objects.get(pk=animal_id)
    datafoto = str(animal.picture).split('/')
    name_foto = datafoto[1]
    predicion = predict(f'media/animal/{name_foto}')

    if predicion == 0:
        resultado = "neumonia por salmonela"
    elif predicion == 1:
        resultado = "Pleuroneumonia Porcina"
    else: 
        resultado = "No se detecto neumonia"

    return render(request, 'result/result.html', {'animal':animal, 'resultado':resultado, 'name_foto':name_foto})