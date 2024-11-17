from django.db import models

class Editorial(models.Model):
    # Datos de la editorial
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    año_creacion = models.IntegerField()
    sitio_web = models.URLField(null=True, blank=True)
    correo_electronico = models.EmailField(null=True, blank=True)
    foto = models.ImageField(upload_to='editoriales/', null=True, blank=True)

    def __str__(self):
        return self.nombre



class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    identificador = models.IntegerField(unique=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero_literario = models.CharField(max_length=100, null=True, blank=True)
    foto = models.ImageField(upload_to='autores/', blank=True, null=True)  # Campo de imagen

    def __str__(self):
        return self.nombre



class Libro(models.Model):
    # Datos básicos del libro
    nombre = models.CharField(max_length=50)
    isbn = models.CharField(max_length=13, unique=True)
    año_lanzamiento = models.CharField(max_length=50)
    numero_paginas = models.IntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    edicion = models.CharField(max_length=50, null=True, blank=True)
    formato = models.CharField(max_length=50, null=True, blank=True)

    # Relación uno a muchos: un libro pertenece a una sola editorial
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, related_name="libros")

    # Relación muchos a muchos: un libro puede tener varios autores
    autores = models.ManyToManyField(Autor, related_name="libros")

    # Añadir un campo de imagen para el libro
    foto = models.ImageField(upload_to='libros/', null=True, blank=True)

    def __str__(self):
        return self.nombre