# Generated by Django 5.1.3 on 2024-11-17 14:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('identificador', models.IntegerField(unique=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('genero_literario', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='autores/')),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
                ('año_creacion', models.IntegerField()),
                ('sitio_web', models.URLField(blank=True, null=True)),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='editoriales/')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('año_lanzamiento', models.CharField(max_length=50)),
                ('numero_paginas', models.IntegerField(blank=True, null=True)),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('edicion', models.CharField(blank=True, max_length=50, null=True)),
                ('formato', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='libros/')),
                ('autores', models.ManyToManyField(related_name='libros', to='appEmpresaLibros.autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='libros', to='appEmpresaLibros.editorial')),
            ],
        ),
    ]
