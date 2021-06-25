from django.urls import path
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('create/', UsuariosCreateView.as_view(), ),
    path('list/', UsuariosFilteredListView.as_view(), ),
    # path('<pk>/detail/', UsuariosDetailView.as_view(), ),
    # path('<pk>/update/', UsuariosUpdateView.as_view(), ),
    # path('<pk>/delete/', UsuariosDeleteView.as_view(), ),
]

