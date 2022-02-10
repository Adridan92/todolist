from django.shortcuts import render
from todolist.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView


# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario: {username} se creo con exito!')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)

def login(request):
    return render(request, 'login.html')


class GetToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user= user)
                if created:
                    return Response({"token": token.key, "message":"Inicio de Sesión Exitoso"}, status = status.HTTP_201_CREATED)
                else:
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({"token": token.key, "message":"Inicio de Sesión Exitoso"}, status = status.HTTP_201_CREATED)
            else:
                return Response({"message": "No esta activo el usuario"}, status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({"message": "Datos incorrectos"}, status = status.HTTP_400_BAD_REQUEST)


class Logout(APIView):

    def post(self, request, *args, **kwargs):
        try:
            token = request.POST.get('token')
            token = Token.objects.filter(key = token).first()        
            if token:
                token.delete()

            return Response({"message":"Se elimino el token"}, status = status.HTTP_200_OK)
        except:
            return Response({"message":"No se encontro el token"}, status = status.HTTP_400_BAD_REQUEST)

    