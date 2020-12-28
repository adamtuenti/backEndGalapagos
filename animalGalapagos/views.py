from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import AnimalModel
from .serializers import analizarImagenSerializer
from django.http import HttpResponse
from rest_framework.response import Response
    
class Animal(APIView):

    def post(self, request, *args, **kwargs):

        #serializer_class = analizarImagenSerializer
       
        #serializer = analizarImagenSerializer(data=request.data)
        imagenAnimal = request.FILES['file']
        print(imagenAnimal)
        salida = {'nombrnimal':imagenAnimal,'accuracy':10,'imagenAnimal':10}
        return Response(data=salida)

    
    def funcion(imagen):
        return ['hola']

            