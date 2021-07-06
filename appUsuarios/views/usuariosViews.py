from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from appUsuarios.serializers import *
from api.logger import log
from api.exceptions import *
from rest_framework import  permissions

class UsuariosCreateView(CreateAPIView):
    # permission_classes = (permissions.AllowAny,)
    serializer_class = UsuarioSerializer

    def post(self, request, *args, **kwargs):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            
            if int(request.data.get('edad')) > 18:   
                request.data['isMayorEdad'] = True
            else: 
                request.data['isMayorEdad'] = False
            
            
            return self.create(request, *args, **kwargs)
        log.info(f'campos incorrectos: {serializer.errors}')
        raise Response400(serializer.errors)
    
