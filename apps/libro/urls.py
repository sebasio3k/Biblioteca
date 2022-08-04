from django.urls import path

from apps.libro.views import CrearAutor, EliminarAutor, ListadoAutores, ActualizarAutor

urlpatterns = [
    path('crear-autor/', CrearAutor.as_view(), name='crear_autor'),
    path('listar-autor/', ListadoAutores.as_view(), name='listar_autor'),
    # path('inicio_autor/', InicioAutor.as_view(), name='inicio_autor'),
    path('editar-autor/<int:pk>', ActualizarAutor.as_view(), name='editar_autor'),
    path('eliminar-autor/<int:pk>', EliminarAutor.as_view(), name='eliminar_autor'),
]
