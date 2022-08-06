from django.db import models


# Create your models here.


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, blank=False, null=False)
    apellidos = models.CharField(max_length=220, blank=False, null=False)
    nacionalidad = models.CharField(max_length=100, blank=False, null=False)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['nombre']

    def __str__(self):
        """ Para identificar a cada objeto instanciado creado """
        return f'{self.nombre} {self.apellidos}'


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=255, blank=False, null=False)
    fecha_publicacion = models.DateField('Fecha de publicación', blank=False, null=False)
    fecha_creacion = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)
    estado = models.BooleanField('Estado', default=True)

    # 1 libro solo puede tener 1 autor:
    # autor_id = models.OneToOneField(Autor, on_delete=models.CASCADE)
    # 1 libro puede ser escrito por uno o mas autores
    # autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE)
    # muchos libros pueden ser escritos por uno o muchos autores
    autor_id = models.ManyToManyField(Autor)

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo
