from rest_framework.test import APITestCase
from appUsuarios.models import *
import json
from rest_framework import status
from django.contrib.auth.models import User


# python manage.py test appUsuarios.tests.PostUsuariosTest --settings=server.settings.dev
class PostUsuariosTest(APITestCase):
    def setUp(self):

        # preparacion de modelo a testiar
        Usuario.objects.create(nombre='lencho', edad=15, isMayorEdad=False)

        # json de prueba
        self.json = {
            "nombre": "juanito",
            "edad": 25
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
        self.assertEqual(2, Usuario.objects.count())

        self.json['nombre'] = True
        response = self.client.post('/api/usuarios/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> 400 - error en json \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # nueva BL  agregar campo 'edad' y isMayorEdad-> verdaero si edad>18
        self.json['nombre'] = 'juanito'
        self.json['edad'] = 10
        self.json['isMayorEdad'] = True

        response = self.client.post('/api/usuarios/create/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> 201-OK \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(3, Usuario.objects.count())
        # self.assertEqual(18, Usuario.objects.get(id=3).edad)


# python manage.py test appUsuarios.tests.GetUsuariosFilteredListTest --settings=server.settings.dev
class GetUsuariosFilteredListTest(APITestCase):
    def setUp(self):
        Usuario.objects.create(nombre='usuario_1', edad=15, isMayorEdad=False)
        Usuario.objects.create(nombre='usuario_2', edad=35, isMayorEdad=True)
        Usuario.objects.create(nombre='usuario_3', edad=18, isMayorEdad=True)

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/api/usuarios/list/')
        print(f'response JSON ===>>> 201-OK \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/usuarios/list/?nombre=usuario_1')
        print(f'response JSON ===>>> 201-OK \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# python manage.py test appUsuarios.tests.GetUsuariosDetailTest --settings=server.settings.dev
class GetUsuariosDetailTest(APITestCase):
    def setUp(self):
        Usuario.objects.create(nombre='usuario_1', edad=15, isMayorEdad=False)
        Usuario.objects.create(nombre='usuario_2', edad=35, isMayorEdad=True)
        Usuario.objects.create(nombre='usuario_3', edad=18, isMayorEdad=True)

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.get('/api/usuarios/3/detail/')
        print(f'response JSON ===>>> 200-OK \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get('/api/usuarios/33/detail/')
        print(f'response JSON ===>>> 404\n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# python manage.py test appUsuarios.tests.PutUsuariosTest --settings=server.settings.dev
class PutUsuariosTest(APITestCase):
    def setUp(self):
        Usuario.objects.create(nombre='usuario_1', edad=15, isMayorEdad=False)
        Usuario.objects.create(nombre='usuario_2', edad=35, isMayorEdad=True)
        Usuario.objects.create(nombre='usuario_3', edad=18, isMayorEdad=True)

        self.json = {
            "nombre": "juanito",
            "edad": 25,
            "isMayorEdad": True
        }

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.put('/api/usuarios/3/update/', data=json.dumps(self.json), content_type="application/json")
        print(f'response JSON ===>>> 200-OK \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual('juanito', Usuario.objects.get(id=3).nombre)


# python manage.py test appUsuarios.tests.DeleteUsuariosTest --settings=server.settings.dev
class DeleteUsuariosTest(APITestCase):
    def setUp(self):
        Usuario.objects.create(nombre='usuario_1', edad=15, isMayorEdad=False)
        Usuario.objects.create(nombre='usuario_2', edad=35, isMayorEdad=True)
        Usuario.objects.create(nombre='usuario_3', edad=18, isMayorEdad=True)

        self.user = User.objects.create_user(username='gabriel', is_staff=True)  # IsAuthenticated

    def test(self):
        self.client.force_authenticate(user=self.user)

        response = self.client.delete('/api/usuarios/3/delete/')
        # print(f'response JSON ===>>> 204- vacio \n {json.dumps(response.json())} \n ---')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(2, Usuario.objects.count())

        cuenta = Usuario.objects.count()
        print(f'--->>>cuenta: {cuenta}')
