from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import permissions
from api.exceptions import *
from django.shortcuts import render
from rest_framework.generics import DestroyAPIView, ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView
from appUsuarios.serializers import *

import logging
log = logging.getLogger('django')


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


class UsuariosFilter(FilterSet):
    class Meta:
        model = Usuario
        fields = ['nombre']


class UsuariosFilteredListView(ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuariosFilteredListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = UsuariosFilter


class UsuariosDetailView(RetrieveAPIView):
    queryset = Usuario.objects.filter()
    serializer_class = UsuarioDetailSerializer


class UsuariosUpdateView(UpdateAPIView):
    queryset = Usuario.objects.filter()
    serializer_class = UsuarioUpdateSerializer


class UsuariosDeleteView(DestroyAPIView):
    queryset = Usuario.objects.filter()
