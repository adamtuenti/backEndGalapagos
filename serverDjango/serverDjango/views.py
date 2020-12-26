from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .models import AnimalModel
from .serializers import analizarImagenSerializer
from django.http import HttpResponse

class Animal(generics.GenericAPIView):

    def analizarImagen(image):

        serializer_class = analizarImagenSerializer
        def post(self, request, *args, **kwargs):
            serializer = analizarImagenSerializer(data=request.data)
            imagenAnimal = request.data.get('imagenAnimal')

            return HttpResponse('primer valor',10,'imagen')
            # serializer.is_valid()
            # usuario = request.data.get('usuario')
            # final=User.objects.filter(id=usuario)
            # user = final.get()
            
            # nombre=User.objects.filter(id=usuario).values('first_name')
            # print(nombre)
            # valor_nombre=nombre.get()
            # print(valor_nombre)
            # firstname=str(valor_nombre.get('first_name'))
            # print(firstname)

            # apellido=User.objects.filter(id=usuario).values('last_name')
            # valor_apellido=apellido.get()
            # lastname=str(valor_apellido.get('last_name'))
            # #user_app = str(user)
            # subject = request.POST.get('', 'Unirse a la Aplicación SolinalFood')
            # message = request.POST.get('', 'El usuario '+ firstname+' '+ lastname +', le ha enviado una invitación para que pueda unirse a la app de SolinalFood')
            # from_email = request.POST.get('','')
            # send_mail(subject, message, from_email, [correo_app])
            # serializer.save()   
            # return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def funcion(imagen):
        return ['hola']

            