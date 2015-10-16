
from django.db import models
from django.contrib.auth.models import User
from GestionPro.apps.usuario.models import Actividad
from django.test import TestCase
from django.utils.datetime_safe import date
# Create your tests here.

class ActividadTest(TestCase):

    def crear_usuario(self, username='sigesproag', first_name= 'vidal', last_name='test', email='sigesproag@gmail.com',password='ingeii', is_superuser=False):
            return User.objects.create(username=username ,first_name= first_name, last_name=last_name, email=email,password= password, is_superuser=is_superuser)



    def test_actividad_creation(self):
        lider = self.crear_usuario()
        lider.save()


        a = Actividad.objects.create(nombre='Actividad de Prueba', descripcion='No existen comentarios', fecha_creacion= date.today(), usuario_creador=lider)
        self.assertTrue(isinstance(a, Actividad))
        self.assertEqual((a.__unicode__()), a.nombre)
        print('Ejecutando test de Actividad')