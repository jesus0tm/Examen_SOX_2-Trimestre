from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import registro_jug
from django.views.decorators.csrf import csrf_exempt
import json

def mi_vista_sin_proteccion_csrf(request):
    # Tu lógica de vista aquí
    return JsonResponse("Esta vista no tiene protección CSRF.")


@csrf_exempt
def introducir_socio(request):
    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_socio = registro_jug(dni=body['dni'], num_socio=body['num_socio'], contraseña=body["contraseña"])
    nuevo_socio.save()
    return JsonResponse({'message': 'Socio introducido correctamente'})

@csrf_exempt
def obtener_todos_socios(request):
    registros_jug = list(registro_jug.objects.values())
    return JsonResponse(registros_jug, safe=False)


