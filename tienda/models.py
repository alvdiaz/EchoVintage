from django.db import models

# Create your models here.
class Vinilo(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    nuevo = models.BooleanField()
    fecha_lanzamiento = models.DateField()
    imagen = models.ImageField(upload_to="vinilos", null=True)

    def __str__(self):
        return self.nombre
    
class Cassette(models.Model):
    nombre_cassete = models.CharField(max_length=50)
    precio_cassete = models.IntegerField()
    descripcion_cassete = models.TextField()
    nuevo_cassete = models.BooleanField()
    fecha_lanzamiento_cassete = models.DateField()
    imagen_cassete = models.ImageField(upload_to="cassettes", null=True)

    def __str__(self):
        return self.nombre_cassete
    
class Cd(models.Model):
    nombre_cd = models.CharField(max_length=50)
    precio_cd = models.IntegerField()
    descripcion_cd = models.TextField()
    nuevo_cd = models.BooleanField()
    fecha_lanzamiento_cd = models.DateField()
    imagen_cd = models.ImageField(upload_to="cds", null=True)

    def __str__(self):
        return self.nombre_cd
    

    