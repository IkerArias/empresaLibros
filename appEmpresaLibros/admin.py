from django.contrib import admin
from .models import Editorial, Autor, Libro

# Registro de los modelos en el admin
admin.site.register(Editorial)
admin.site.register(Autor)
admin.site.register(Libro)
