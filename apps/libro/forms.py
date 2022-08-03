from django import forms

from apps.libro.models import Autor


class AutorForm(forms.ModelForm):
    """ Hereda campos de modelo (ModelForm) """

    class Meta:
        model = Autor
        fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
