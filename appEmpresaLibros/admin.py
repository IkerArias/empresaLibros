from django.contrib import admin
from .models import Editorial, Autor, Libro


admin.site.site_header = "Book-Store Administration"
admin.site.site_title = "Custom Admin"




@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais', 'id')
    

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('nombre','isbn', 'precio', 'edicion')

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais', 'año_creacion')

    def año_creacion(self, obj):
        return obj.año_creacion  
    año_creacion.short_description = 'Año de Creación'
