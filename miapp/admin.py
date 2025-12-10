from django.contrib import admin
from .models import Practica, Anime

# Register your models here.
from .models import Practica

@admin.register(Practica)
class PracticaAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "password")  # columnas que quieres ver
    search_fields = ("username",)                  # barra de búsqueda
    list_filter = ("username",)                    # filtros opcionales

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "genero", "calidad", "rating", "episodios")
    search_fields = ("nombre", "genero")
    list_filter = ("calidad", "genero")