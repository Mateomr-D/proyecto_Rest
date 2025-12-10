from django.db import models

class Practica(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    imagen = models.URLField(max_length=500, blank=True, null=True)
    
    def _str_(self):
        return self.username
    


class Anime(models.Model):
    CALIDAD_CHOICES = [
        ('SUB', 'Subtitulado'),
        ('DUB', 'Doblado'),
        ('RAW', 'Raw'),
    ]
    
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.URLField(max_length=500)
    episodios = models.IntegerField(default=1)
    calidad = models.CharField(max_length=3, choices=CALIDAD_CHOICES, default='SUB')
    genero = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def _str_(self):
        return self.nombre
    
    class Meta:
        ordering = ['-fecha_creacion']