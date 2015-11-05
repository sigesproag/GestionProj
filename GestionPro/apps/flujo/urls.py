# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url
from django.conf.urls import *
from django.views.generic import *
from django.contrib.auth.models import User
from django.template import *
import os.path

from GestionPro.apps.flujo.forms import *
from GestionPro.apps.flujo.models import *
from GestionPro.apps.flujo.views import *

urlpatterns = patterns('GestionPro.apps.flujo.views',
	url(r'^flujos/$', 'admin_flujo', name='vista_admiF'),
	url(r'^verFlujo/ver&id=(?P<flujo_id>\d+)/$', 'visualizar_flujo', name='vista_flujo'),
	url(r'^crearFlujo/$','crear_flujo',name='vista_crearFlujo'),
	url(r'^modificarFlujo/mod&id=(?P<flujo_id>\d+)/$','mod_flujo',name='vista_modFlujo'),
	url(r'^eliminarFlujo/del&id=(?P<flujo_id>\d+)/$','borrar_flujo',name='vista_delFlujo'),
    url(r'^asignarActividad/actividad&id=(?P<flujo_id>\d+)/$','asignar_actividades',name='vista_asignarActividad'),
    url(r'^bajarActividad/flujo&id=(?P<flujo_id>\d+)&&actividad&id=(?P<actividad_id>\d+)/$','bajar_actividad',name='vista_bajarActividad'),
    url(r'^subirActividad/flujo&id=(?P<flujo_id>\d+)&&actividad&id=(?P<actividad_id>\d+)/$','subir_actividad',name='vista_subirActividad')

)


