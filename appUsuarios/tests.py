from rest_framework.test import APITestCase
from appUsuarios.models import *
import json
from rest_framework import status
from django.contrib.auth.models import User


class PostUsuariosTest(APITestCase):
    def setUp(self):
       
        # preparacion de modelo a testiar 
        Usuario.objects.create(nombre='lencho')
        
        # json de prueba
        self.json = {
            "nombre": "juanito"
        }

        # autenticaciones
        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated
    
    # Declaracion de pruebas -> pueden ir aumentando 
    def test(self):
        response = self.client.post('/api/usuarios/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> 401- no autenticado \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
        self.client.force_authenticate(user=self.user)
        
        response = self.client.post('/api/usuarios/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> 201-OK \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(2, Usuario.objects.count())
        
        self.json['nombre'] = True
        response = self.client.post('/api/usuarios/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> 400 - error en json \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


# python manage.py test appUsuarios.test.PostUsuariosTest --settings=server.settings.local