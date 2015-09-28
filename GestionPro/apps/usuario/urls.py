# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url
from django.conf.urls import *
from django.views.generic import *
from django.contrib.auth.models import User
from django.template import *
import os.path

from GestionPro.apps.usuario.forms import *
from GestionPro.apps.usuario.models import *
from GestionPro.apps.usuario.views import *

urlpatterns = patterns('GestionPro.apps.usuario.views',
	url(r'^admin/$', 'admin_usuarios', name='vista_adminU'),
	url(r'^visualizar/ver&id=(?P<usuario_id>\d+)/$', 'visualizar_usuario', name='vista_usuario'),
	url(r'^crear/$','crearUsuario_view',name='vista_crearUsuario'),
	url(r'^lista/(?P<tipo>\w+)/$', 'lista', name='vista_lista'),
	url(r'^modificar/mod&id=(?P<usuario_id>\d+)/$','mod_user',name='vista_modUsuario'),
    	url(r'^eliminar/eli&id=(?P<usuario_id>\d+)/$','eliminar_usuario',name='vista_eliUsuario'),
    	url(r'^activar/act&id=(?P<usuario_id>\d+)/$','activar_usuario',name='vista_actUsuario'),
	#url(r'^borrar/del&id=(?P<usuario_id>\d+)/$','borrar_usuario',name='vista_delUsuario'),
	url(r'^cambiarcontrasena/$','cambiar_password',name='vista_cambiarContrasena'),
    	url(r'^asignarRol/rol&id=(?P<usuario_id>\d+)/$','asignar_roles_sistema',name='vista_asignarRol'),
	url(r'^asignarRolP/rol&id=(?P<usuario_id>\d+)/$','asignar_roles_proyecto',name='vista_asignarRolP')
)

