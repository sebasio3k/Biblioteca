from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Autor, Libro


class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor


class LibroResource(resources.ModelResource):
    class Meta:
        model = Libro


class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Barra de busqueda:
    search_fields = ['nombre', 'apellidos', 'nacionalidad']
    # Para atributos en vista de registros:
    list_display = [
        'id',
        'nombre',
        'apellidos',
        'nacionalidad',
        'descripcion',
        'estado',
    ]
    resource_class = AutorResource


class LibroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Barra de busqueda:
    search_fields = ['titulo', 'fecha_publicacion']
    # Para atributos en vista de registros:
    list_display = [
        'id',
        'titulo',
        'fecha_publicacion',
        'fecha_creacion',
        'estado',
    ]
    resource_class = AutorResource


# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
