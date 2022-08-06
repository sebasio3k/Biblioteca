from django import forms

from apps.libro.models import Autor, Libro


class AutorForm(forms.ModelForm):
    """ Hereda campos de modelo (ModelForm) """

    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
        labels = {
            'nombre': 'Nombre del autor',
            'apellidos': 'Apellidos del autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion': 'Pequeña descripción',
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe el nombre del autor',
                    'id': 'nombre',
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe los apellidos del autor',
                    'id': 'apellidos',
                }
            )
            , 'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe la nacionalidad del autor',
                    'id': 'nacionalidad',
                }
            )
            , 'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pequeña descripción del autor',
                    'id': 'descripcion',
                }
            ),
        }


class LibroForm(forms.ModelForm):
    """ Hereda campos de modelo (ModelForm) """

    class Meta:
        model = Libro
        fields = ['titulo', 'fecha_publicacion', 'autor_id']
        labels = {
            'titulo': 'Título del libro',
            'fecha_publicacion': 'Fecha de publicación del libro',
            'autor_id': 'Autor(es) del libro',
        }
        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe el título del libro',
                    'id': 'titulo',
                }
            ),
            'fecha_publicacion': forms.SelectDateWidget(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona la fecha de publicación del libro',
                    'id': 'fecha_publicacion',
                }
            )
            , 'autor_id': forms.SelectMultiple(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Selecciona el/los autor(es) del libro',
                    'id': 'autor_id',
                }
            )
            ,
        }
