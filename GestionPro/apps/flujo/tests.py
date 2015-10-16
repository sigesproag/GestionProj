# Create your tests here
from django.db import models
from django.test import TestCase
from django.contrib.auth.models import User
from GestionPro.apps.usuario.models import Flujo
from django.utils.datetime_safe import date


class FlujosTest(TestCase):
    def crear_usuario(self, username='sigesproag', first_name='vidal', last_name='test',
                      email='sigesproag@gmail.com', password='ingeii', is_superuser=False):
        return User.objects.create(username=username, first_name=first_name, last_name=last_name,
                                   email=email, password=password, is_superuser=is_superuser)

    def test_flujos_creation(self):
        lider = self.crear_usuario()
        lider.save()

        f = Flujo.objects.create(nombre='Flujo de Prueba', descripcion='No existen comentarios',
                                 fecha_creacion=date.today(), usuario_creador=lider)
        self.assertTrue(isinstance(f, Flujo))
        self.assertEqual((f.__unicode__()), f.nombre)
        print('Ejecutando test de Flujos')