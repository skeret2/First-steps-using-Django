from django.shortcuts import render

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hola estoy en el get", status=200) # respuesta del servicio
    
    def patch(self, request):
        return Response(data="Hola estoy en el patch", status=200)
    
    def delete(self, request):
        return Response(data="Hola estoy en el delete", status=200)
    
    def post(self, request):
        return Response(data="Hola gente estoy en el post", status=200)

class PetListAPIView(ListAPIView):
    def get(self, request):
        return Response(data="Hola estas son todas mis mascotas", status=200)

class PetAPIView(RetrieveAPIView):
    def get(self, request):
        return Response(data="Hola estoy en el post", status=200)



