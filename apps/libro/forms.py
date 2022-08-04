from django import forms

from apps.libro.models import Autor


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
            ,'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Escribe la nacionalidad del autor',
                    'id': 'nacionalidad',
                }
            )
            ,'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Pequeña descripción del autor',
                    'id': 'descripcion',
                }
            ),
        }
