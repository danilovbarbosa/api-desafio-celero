import json
from profile import Profile

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from historia_olimpica.models import NocRegions, AthleteEvents
from historia_olimpica.serializers import NocRegionsSerializer, AthleteEventsSerializer
from historia_olimpica.views import NocRegionsViewSet


class RegistrosTestCase(APITestCase):
    def test_registro_de_noc_regions_deve_retornar_status_201(self):
        data = {
            "noc": "teste",
            "region": "teste",
            "notes": "teste"
        }
        response = self.client.post('/historia_olimpica/noc_regions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class NocRegionsViewSetTestCase(APITestCase):

    list_url = reverse('noc_regions-list')
    detail_url = reverse('noc_regions-detail', kwargs={'pk': 0})

    def setUp(self):
        self.user = User.objects.create_user(username='teste',
                                             password='teste')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_noc_regions_autenticacao_lista_deve_retornar_status_200(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_noc_regions_detail_retrieve_deve_retornar_status_200(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
