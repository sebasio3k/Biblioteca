from django.urls import path

from apps.libro.views import crearAutor, listarAutor, editarAutor, eliminarAutor

urlpatterns = [
    path('crear-autor/', crearAutor, name='crear_autor'),
    path('listar-autor/', listarAutor, name='listar_autor'),
    path('editar-autor/<int:id>', editarAutor, name='editar_autor'),
    path('eliminar-autor/<int:id>', eliminarAutor, name='eliminar_autor'),
]
