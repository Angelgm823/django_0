from django.db import models

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

    def __str__(self):
        return self.titulo


class DetallesLibro(models.Model):
    resumen = models.TextField()
    portada_url = models.CharField()
    lenguaje = models.CharField()
    libro = models.OneToOneField(Libros, on_delete=models.CASCADE, related_name='detalle')