from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    # CASCADE: eliminar el producto si se elimina la categoria
    # PROTECT: lanza un error no te deja eliminar la categoria
    # RESTRICTIC: solo elimina si no existe el producto
    # SET_NULL: actualiza a valor nulo
    # SET_DEFAULT: asigna el valor por defecto 
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
