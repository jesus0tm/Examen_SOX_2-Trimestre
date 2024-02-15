def introducir_socio(request):
    string_body = request.body.decode('utf8').replace("'", '"') 
    body = json.loads(string_body)
    #pdb.set_trace()
    nuevo_socio = registro_jug(dni=body['dni'], num_socio=body['num_socio'], contraseña=body["contraseña"])
    nuevo_socio.save()
    return JsonResponse({'message': 'Socio introducido correctamente'})
