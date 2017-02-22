from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Publicacion
from modules.Usuarios.models import User
import json



class PublicacionListTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(email="user1@gmail.com",password="Blog123456")
        self.data = {"nombre":"Otra Publicacion","contenido":"asdasdsadsadasdasdsda","tags":"TC","autor":self.user.id_usuario}
        self.url = reverse('api-list-publicacion')

    def test_list_plublicaciones(self):       
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    
    def test_create_publicacion(self):
       response = self.client.post(self.url,self.data,format='json')
       self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class PubicacionDetailTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_superuser(email="user1@gmail.com",password="Blog123456")
        self.publicacion = Publicacion(nombre="Otra Publicacion",contenido="asdasdsadsadasdasdsda",
        tags="TC",autor=self.user)
        self.publicacion.save()
        self.url= reverse('api-detail-publicacion',args=[self.publicacion.id])
    
    def test_retrieve_publicacion(self):
    
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_publicacion(self):
        self.data = {"nombre":"Otra Publicacion","contenido":"asdasdsadsadasdasdsda","fecha":"2017-02-21","tags":"PR","autor":3}    
        response = self.client.put(self.url,self.data,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response.data,self.data)

    def test_delete_publicacion(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
    

# Create your tests here.
