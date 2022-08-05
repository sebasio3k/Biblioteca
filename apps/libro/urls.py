from django.contrib.auth.decorators import login_required
from django.urls import path

from apps.libro.views import CrearAutor, EliminarAutor, ListadoAutores, ActualizarAutor

urlpatterns = [
    path('crear-autor/', login_required(CrearAutor.as_view()), name='crear_autor'),
    path('listar-autor/', login_required(ListadoAutores.as_view()), name='listar_autor'),
    # path('inicio_autor/', InicioAutor.as_view(), name='inicio_autor'),
    path('editar-autor/<int:pk>', login_required(ActualizarAutor.as_view()), name='editar_autor'),
    path('eliminar-autor/<int:pk>', login_required(EliminarAutor.as_view()), name='eliminar_autor'),
]
