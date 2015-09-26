# -*- coding: utf-8 -*-
from django.conf.urls import patterns,url
from django.conf.urls import *
from django.views.generic import *
from django.contrib.auth.models import User
from django.template import *
import os.path

from GestionPro.apps.roles.forms import *
from GestionPro.apps.roles.models import *
from GestionPro.apps.roles.views import *

urlpatterns = patterns('GestionPro.apps.roles.views',
	url(r'^roles/$', 'admin_roles', name='vista_adminR'),
	url(r'^rolesSist/$', 'admin_roles_sist', name='vista_adminRS'),
	url(r'^rolesProy/$', 'admin_roles_proy', name='vista_adminRP'),
	url(r'^verRol/ver&id=(?P<rol_id>\d+)/$', 'visualizar_roles', name='vista_roles'),
	url(r'^crearRolS/$','crear_rolS',name='vista_crearRolS'),
	url(r'^crearRolP/$','crear_rolP',name='vista_crearRolP'),
	url(r'^modificarRol/mod&id=(?P<rol_id>\d+)/$','mod_rol',name='vista_modRol'),
	url(r'^eliminarRol/del&id=(?P<rol_id>\d+)/$','borrar_rol',name='vista_delRol'),
	url(r'^roles/permisos&id=(?P<rol_id>\d+)/$','admin_permisos',name='vista_permisos')
)

