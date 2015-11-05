from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^demo/', include('demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^',include('GestionPro.apps.home.urls')),
    url(r'^',include('GestionPro.apps.usuario.urls')),
    url(r'^',include('GestionPro.apps.roles.urls')),
    url(r'^',include('GestionPro.apps.flujo.urls')),
    url(r'^',include('GestionPro.apps.proyectos.urls')),
    url(r'^',include('GestionPro.apps.sprint.urls')),
    url(r'^',include('GestionPro.apps.actividades.urls')),
    url(r'^',include('GestionPro.apps.userhistory.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
