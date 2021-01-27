import json
from profile import Profile

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from historia_olimpica.models import NocRegions, AthleteEvents
from historia_olimpica.serializers import NocRegionsSerializer, AthleteEventsSerializer

class RegistrosTestCase(APITestCase):
    def test_registro_de_noc_regions_deve_retornar_status_200(self):
        data = {
            "noc": "teste",
            "region": "teste",
            "notes": "teste"
        }
        response = self.client.post('/historia_olimpica/noc_regions/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)