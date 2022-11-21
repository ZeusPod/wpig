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
    
    #obtenemos los datos a guardar en los resultados
    age = str(animal.age)
    description = str(animal.description)
    picture = name_foto
    dueño = str(animal.user_id)
    establo = str(animal.establo)
    galpon = str(animal.galpon)
    raza = str(animal.raza)
    register_date = str(animal.register_date)
    born_date = str(animal.born_date)
    place_of_birth = str(animal.place_of_birth)

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
        r = Resultados(animal_id= dueño ,age=age, description=description, name_foto= picture, establo=establo,galpon= galpon, raza=raza,register_date=register_date,born_date=born_date,place_of_birth=place_of_birth, resultado=resultado, sintomas=sintomas, recomendaciones=recomendaciones)
        r.save()

        

    return render(request, 'result/result.html', {'animal':animal, 'resultado':resultado, 'name_foto':name_foto, 'sintomas':sintomas, 'recomendaciones':recomendaciones})


# Get all results
def get_results(request):
    results = Resultados.objects.all()
    return render(request, 'result/list_result.html', {"results":results})


# Get results by user_id
def get_results_by_id(request, username):
    data = Resultados.objects.filter(animal_id=username)
    resp = data[0:]
    return render(request, 'result/list_client.html', {'resp':resp})

#details informe
def detail_result(request, result_id):
    data = Resultados.objects.get(pk=result_id)
    return render(request,'result/detail_result.html',{'data':data})