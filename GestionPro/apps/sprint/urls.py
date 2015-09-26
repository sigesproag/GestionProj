# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url
from django.conf.urls import *
from django.views.generic import *
from django.contrib.auth.models import User
from django.template import *
import os.path

from GestionPro.apps.sprint.forms import *
from GestionPro.apps.usuario.models import *
from GestionPro.apps.sprint.views import *

urlpatterns = patterns('GestionPro.apps.sprint.views',
	url(r'^sprint/sprint&id=(?P<proyecto_id>\d+)/$', 'admin_sprint', name='vista_adminS'),
	url(r'^verSprint/ver&id=(?P<sprint_id>\d+)/$', 'visualizar_sprint', name='vista_sprint'),
	url(r'^crearSprint/crear&id=(?P<proyecto_id>\d+)/$', 'crear_sprint', name='vista_crearS'),
	url(r'^modificarSprint/mod&id=(?P<sprint_id>\d+)/$','mod_sprint',name='vista_modSprint'),
	url(r'^eliminarSprint/del&id=(?P<sprint_id>\d+)/$','borrar_sprint',name='vista_delSprint')
    #url(r'^eliminarMiembro/del&id=(?P<miembro_id>\d+)/$','borrar_miembro',name='vista_delMiembro'),
	#url(r'^proyectos/flujos&id=(?P<rol_id>\d+)/$','admin_flujos',name='vista_flujos'),
	#url(r'^asignarMiembro/proyecto&id=(?P<proyecto_id>\d+)/$','asignar_miembro',name='vista_miembros'),
    #url(r'^asignarFlujo/proyecto&id=(?P<proyecto_id>\d+)/$','asignar_flujo',name='vista_asignarflujo'),
	#url(r'^modificarMiembro/miembro&id=(?P<proyecto_id>\d+)/$','mod_miembro',name='vista_modMiembro')
)