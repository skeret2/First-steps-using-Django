from django.shortcuts import render

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hola estoy en el get", status=200) # respuesta del servicio

class PetListView(APIView):
    def get(self, request):
        return Response(data="Hola estas son todas mis mascotas", status=200)
    
    def patch(self, request):
        return Response(data="Hola estoy en el patch pets", status=200)
    
    def delete(self, request):
        return Response(data="Hola estoy en el delete pets", status=200)
    
    def post(self, request):
        return Response(data="Hola gente estoy en el post pets", status=200)

class PersonView(APIView):
    def get(self, request):
        return Response(data="Hola estoy en el get person", status=200)
    
    def patch(self, request):
        return Response(data="Hola estoy en el patch person", status=200)
    
    def delete(self, request):
        return Response(data="Hola estoy en el delete person", status=200)
    
    def post(self, request):
        return Response(data="Hola gente estoy en el post person", status=200)



