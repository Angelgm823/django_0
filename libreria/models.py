from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

class Libros(models.Model):
    titulo = models.CharField(max_length=250)
    fecha_publicacion = models.DateField(null=True, blank=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")
    paginas = models.IntegerField()
    isbn = models.CharField(max_length=60)
    generos = models.ManyToManyField(Genero, related_name='libros')
    recomendacion_by = models.ManyToManyField(get_user_model(), through='Recomendaciones', related_name='libros_recomendados')

class Meta:
    verbose_name = 'Libro'
    verbose_name_plural = 'Libros'

    def __str__(self):
        return self.titulo


class DetallesLibro(models.Model):
    resumen = models.TextField()
    portada_url = models.CharField()
    lenguaje = models.CharField()
    libro = models.OneToOneField(Libros, on_delete=models.CASCADE, related_name='detalle')


class Critica(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    libro = models.ForeignKey(Libros, on_delete=models.CASCADE, related_name='critica')
    calificacion = models.PositiveBigIntegerField()
    texto = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario} -> {self.libro.titulo} ({self.calificacion})'


class Prestamo(models.Model):
     usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
     libro = models.ForeignKey(Libros, on_delete=models.CASCADE, related_name='prestamos')
     fecha_prestamo = models.DateTimeField(auto_now_add=True)
     fecha_ingreso = models.DateTimeField(null=True, blank=True)
     estado = models.BooleanField(default=False)

     def __str__(self):
         return f'{self.usuario} -> {self.libro.titulo} ({'Devuelto' if self.estado else 'Prestado'})'


class Recomendaciones(models.Model):
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    libro = models.ForeignKey(Libros, on_delete=models.CASCADE)
    recomendacion_at = models.DateTimeField(auto_now_add=True)
    nota = models.TextField(blank=True)

    class Meta:
        unique_together = ('usuario', 'libro')