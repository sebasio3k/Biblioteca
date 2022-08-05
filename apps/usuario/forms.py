from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'

    # class Meta:
    #     model = Autor
    #     fields = ['nombre', 'apellidos', 'nacionalidad', 'descripcion']
    #     labels = {
    #         'nombre': 'Nombre del autor',
    #         'apellidos': 'Apellidos del autor',
    #         'nacionalidad': 'Nacionalidad del autor',
    #         'descripcion': 'Pequeña descripción',
    #     }
    #     widgets = {
    #         'nombre': forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Escribe el nombre del autor',
    #                 'id': 'nombre',
    #             }
    #         ),
    #         'apellidos': forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Escribe los apellidos del autor',
    #                 'id': 'apellidos',
    #             }
    #         )
    #         , 'nacionalidad': forms.TextInput(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Escribe la nacionalidad del autor',
    #                 'id': 'nacionalidad',
    #             }
    #         )
    #         , 'descripcion': forms.Textarea(
    #             attrs={
    #                 'class': 'form-control',
    #                 'placeholder': 'Pequeña descripción del autor',
    #                 'id': 'descripcion',
    #             }
    #         ),
    #     }
