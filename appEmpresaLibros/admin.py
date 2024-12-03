from django.contrib import admin
from .models import Editorial, Autor, Libro


admin.site.site_header = "Book-Store Administration"
admin.site.site_title = "Custom Admin"




@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais', 'id')
    search_fields = ('pais', 'nombre','identificador','genero_literario')
    

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('nombre','isbn', 'precio', 'edicion')
    search_fields = ('isbn', 'nombre','edicion','precio')

@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais', 'año_creacion')
    search_fields = ('año_creacion', 'nombre','pais')

    def año_creacion(self, obj):
        return obj.año_creacion  
    año_creacion.short_description = 'Año de Creación'
