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
        imagenAnimal = request.data.get('idAnimal')
        
        print(imagenAnimal)
        idA = 0
        datos = AnimalModel.objects.filter(idAnimal=idA)
        print(datos[0].idAnimal,datos[0].nombreAnimal)

        salida = {'nombrnimal':datos[0].nombreAnimal,'nombreTecnico':datos[0].nombreTecnico},'imagenAnimal':datos[0].imagenAnimal}
        return Response(data=salida)

    
    def funcion(imagen):
        return ['hola']
    
# class DetalleAnimal(RetrieveAPIView):
#     serializer_class = analizarImagenSerializer
#     queryset = AnimalModel.objects.all()



            