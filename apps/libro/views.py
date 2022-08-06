from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView

from apps.libro.forms import AutorForm, LibroForm

from apps.libro.models import Autor, Libro


# Create your views here.
class Inicio(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        libros = Libro.objects.filter(estado=True).count()
        autores = Autor.objects.filter(estado=True).count()
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['libros'] = libros
        context['autores'] = autores
        return context


""" Autores """


class ListadoAutores(ListView):
    model = Autor
    template_name = 'libro/autor/listar_autor.html'
    context_object_name = 'autores'  # nombre de lista de objetos a mandar en template
    queryset = Autor.objects.filter(estado=True).order_by('-id')


class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/autor/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Registrar'
        return context


class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/autor/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar'
        return context


class EliminarAutor(DeleteView):
    """ Eliminación directa: """
    model = Autor

    # success_url = reverse_lazy('libro:listar_autor')

    def post(self, request, pk, *args, **kwargs):
        """ Eliminación lógica """
        instance = Autor.objects.get(id=pk)
        instance.estado = False
        instance.save()
        return redirect('libro:listar_autor')


""" Libro """


class ListadoLibros(ListView):
    model = Libro
    template_name = 'libro/libro/listar_libro.html'
    context_object_name = 'libros'  # nombre de lista de objetos a mandar en template
    queryset = Libro.objects.filter(estado=True).order_by('-id')


class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro/libro/crear_libro.html'
    success_url = reverse_lazy('libro:listar_libro')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Registrar'
        return context


class ActualizarLibro(UpdateView):
    model = Libro
    template_name = 'libro/libro/crear_libro.html'
    form_class = LibroForm
    success_url = reverse_lazy('libro:listar_libro')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar'
        return context


class EliminarLibro(DeleteView):
    """ Eliminación directa: """
    model = Libro

    # success_url = reverse_lazy('libro:listar_libro')

    def post(self, request, pk, *args, **kwargs):
        """ Eliminación lógica """
        instance = Libro.objects.get(id=pk)
        instance.estado = False
        instance.save()
        return redirect('libro:listar_libro')
