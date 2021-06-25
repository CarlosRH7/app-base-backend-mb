from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from appUsuarios.serializers import *
from api.logger import log
from api.exceptions import *
from rest_framework import  permissions

class UsuariosCreateView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = UsuarioSerializer

class UsuariosFilteredListView(CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    
