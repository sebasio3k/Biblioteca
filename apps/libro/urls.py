from django.urls import path

from apps.libro.views import crearAutor, listarAutor, editarAutor, eliminarAutor, ListadoAutores

urlpatterns = [
    path('crear-autor/', crearAutor, name='crear_autor'),
    path('listar-autor/', ListadoAutores.as_view(), name='listar_autor'),
    # path('inicio_autor/', InicioAutor.as_view(), name='inicio_autor'),
    path('editar-autor/<int:id>', editarAutor, name='editar_autor'),
    path('eliminar-autor/<int:id>', eliminarAutor, name='eliminar_autor'),
]
