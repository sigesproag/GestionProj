from django.test import TestCase

# Create your tests here.
from django.db import models
from django.contrib.auth.models import User
from GestionPro.apps.usuario.models import Flujo, Proyecto, UserHistory, Sprint, Actividad
from django.test import TestCase
from django.utils.datetime_safe import date

class UserHistoryTest(TestCase):

    def crear_usuario(self, username='sigesproag', first_name= 'vidal', last_name='test', email='sigesproag@gmail.com',password='ingeii', is_superuser=False):
            return User.objects.create(username=username ,first_name= first_name, last_name=last_name, email=email,password= password, is_superuser=is_superuser)


    def test_us_creation(self):
        lider = self.crear_usuario()
        lider.save()
        flujo = Flujo.objects.create(nombre='Flujo Test', descripcion='No existen comentarios', fecha_creacion= date.today(), usuario_creador=lider)
        flujo.save()
        proyecto = Proyecto.objects.create(nombrelargo='Proyecto Iniciado', usuario_lider=lider, descripcion='Proyecto Prueba', fecha_inicio=date.today(), fecha_fin=date.today(), cantidad = 1, estado='2')
        proyecto.save()

        sprint = Sprint.objects.create(proyecto=proyecto, nombre='Sprint Prueba', descripcion='No existen comentarios', fecha_inicio=date.today(), fecha_fin=date.today())
        sprint.save()

        actividad = Actividad.objects.create(nombre='Actividad de Prueba', descripcion='No existen comentarios', fecha_creacion= date.today(), usuario_creador=lider)

        us = UserHistory.objects.create(nombre='User History Prueba', valor_tecnico=0, valor_negocio=0, prioridad=1, proyecto=proyecto, flujo=flujo, actividad = actividad, sprint=sprint, estado=1, tiempo_estimado=10,tiempo_utilizado=0)
        self.assertTrue(isinstance(us, UserHistory))
        self.assertEqual((us.__unicode__()), us.nombre)
        print('Ejecutando test de UserHistory')