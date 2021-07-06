from rest_framework.test import APITestCase
from appUsuarios.models import *
import json
from rest_framework import status
from django.contrib.auth.models import User


# python manage.py test appUsuarios.tests.PostUsuariosTest --settings=server.settings.local
class PostUsuariosTest(APITestCase):
    def setUp(self):
        Usuario.objects.create(nombre='lencho')
        
        self.json = {
            "nombre": "juanito"
        }
        
        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated
    
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

