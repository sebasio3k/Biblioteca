from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, CreateView, UpdateView, DeleteView

from apps.libro.forms import AutorForm

from apps.libro.models import Autor


# Create your views here.
class Inicio(TemplateView):
    template_name = 'index.html'


class ListadoAutores(ListView):
    model = Autor
    template_name = 'libro/listar_autor.html'
    context_object_name = 'autores'  # nombre de lista de objetos a mandar en template
    queryset = autores = Autor.objects.filter(estado=True).order_by('-id')


class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'libro/crear_autor.html'
    success_url = reverse_lazy('libro:listar_autor')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Registrar'
        return context


class ActualizarAutor(UpdateView):
    model = Autor
    template_name = 'libro/crear_autor.html'
    form_class = AutorForm
    success_url = reverse_lazy('libro:listar_autor')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['accion'] = 'Editar'
        return context


class EliminarAutor(DeleteView):
    pass


""" VISTAS BASADAS EN FUNCIONES: 

def crearAutor(request):
    if request.method == 'POST':
        #   1 Forma de crear: 
        #     nom = request.POST.get('nombre')
        #     ape = request.POST.get('apellidos')
        #     nacio = request.POST.get('nacionalidad')
        #     desc = request.POST.get('descripcion')
        #     autor = Autor(nombre=nom, apellidos=ape, nacionalidad=nacio, descripcion=desc)
        #     autor.save()
        #     return redirect('libro:listar_autor')
        #
        # return render(request, 'libro/crear_autor.html', {'accion': 'Crear'})

        # otra forma usando forms
        print(request.POST)
        autor_form = AutorForm(request.POST)  # datos = request.POST
        if autor_form.is_valid():
            # nom = autor_form.cleaned_data['nombre']
            autor_form.save()  # guardar en BD
            #     # return redirect('index')  # index = name en urls
            return redirect('libro:listar_autor')
    else:
        autor_form = AutorForm()
        # print(autor_form)
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'accion': 'Crear'})
    # return render(request, 'libro/crear_autor.html', {'accion': 'Crear'})

def listarAutor(request):
    # autores = Autor.objects.all().order_by('-id')
    autores = Autor.objects.filter(estado=True).order_by('-id')  # para implementar eliminacion lógica

    return render(request, 'libro/listar_autor.html', {'autores': autores})


def editarAutor(request, id):
    autor_form = None
    error = None

    try:
        autor = Autor.objects.get(id=id)
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)

        else:
            autor_form = AutorForm(request.POST, instance=autor)
            if autor_form.is_valid():
                autor_form.save()
            return redirect('libro:listar_autor')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form, 'accion': 'Editar', 'error': error})


def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == 'POST':
        # ELIMINACION DIRECTA:
        # autor.delete()  # borrar de la BD
        # ELIMINACION LÓGICA:
        autor.estado = False
        autor.save()
        return redirect('libro:listar_autor')
    return render(request, 'libro/eliminar_autor.html', {'autor': autor})
"""
