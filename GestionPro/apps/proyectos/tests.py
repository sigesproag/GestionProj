
# Create your tests here.
import unittest
from django.test import Client, TestCase
from django.core.urlresolvers import reverse
from django.utils.datetime_safe import date
from GestionPro.apps.proyectos.forms import ProyectoForm
from GestionPro.apps.usuario.models import Proyecto
from GestionPro.apps.usuario.models import User


class ProyectoTest(TestCase):

    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_lista(self):
        # Issue a GET request.
        response = self.client.get('/proyectos/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)