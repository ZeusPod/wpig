from django.shortcuts import render
from animal.models import Animal
from utils.neuronal import predict
from sintomas.models import Sintomas
from recomendaciones.models import Recomendaciones
from django.contrib import messages
from result.models import Resultados


# Process image
def process_image(request,animal_id):
    animal = Animal.objects.get(pk=animal_id)
    datafoto = str(animal.picture).split('/')
    name_foto = datafoto[1]
    predicion = predict(f'media/animal/{name_foto}')
    print(predicion)
    if predicion == 0:
        resultado = "neumonia por salmonela"
    elif predicion == 1:
        resultado = "Pleuroneumonia Porcina"
    else: 
        resultado = "No se detecto neumonia"

    sintomas = Sintomas.objects.get(pk=predicion + 1)
    recomendaciones = Recomendaciones.objects.get(pk=predicion + 1)

    if predicion == 0 or predicion == 1:
        messages.success(request, 'El resultado a sido generado con exito') 


        #Guardando el result
        r = Resultados(animal_id=animal, name_foto=animal.picture, resultado=resultado, sintomas=sintomas, recomendaciones=recomendaciones)
        r.save()

    return render(request, 'result/result.html', {'animal':animal, 'resultado':resultado, 'name_foto':name_foto, 'sintomas':sintomas, 'recomendaciones':recomendaciones})


# Get all results
def get_results(request):
    results = Resultados.objects.all()
    return render(request, 'result/list_result.html', {"results":results})

