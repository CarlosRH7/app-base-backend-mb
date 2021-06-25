from django.shortcuts import render

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Semilla API",
        default_version='v1',
        description="Estructura de proyecto base.",
        terms_of_service="#",
        contact=openapi.Contact(email="name.developer@mb.company"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

