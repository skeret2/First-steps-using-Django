from django.shortcuts import render

# modulos de DRF
from rest_framework.response import Response
from rest_framework.views import APIView

class HelloWorld(APIView):
    def get(self, request): # verbo de la peticion como un metodo
        # logica asociada al endpoint
        return Response(data="Hello, World !", status=200) # respuesta del servicio
y en urls.py eliminamos el path del admin y añadimos nuestra view asi:

from django.contrib import admin
from django.urls import path, include

from petclub.views import HelloWorld

urlpatterns = [
    path('hi', HelloWorld.as_view(), name="helloworld"),
    path('api-auth/', include('rest_framework.urls')),
]

