from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language  # Añadir esto

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Agregar la URL para el cambio de idioma
urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),  # Esta línea es la clave
]

# Aplica i18n_patterns a los patrones de URL de la app
urlpatterns += i18n_patterns(
    path('appEmpresaLibros/', include('appEmpresaLibros.urls')),
)

# Servir archivos estáticos y de medios en modo debug
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
