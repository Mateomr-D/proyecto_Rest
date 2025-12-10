from django.urls import path
from . import views

urlpatterns = [
    
    path("principal/", views.Vista1, name="vista1"),
    path("vista/", views.Vista2, name="vista2"),
    path("formulario/", views.formulario,  name="formulario"),
    path("login/", views.login,  name="login"),
    path("usuarios/", views.usuarios,  name="usuarios"),
    path("actualizar/<int:id>/", views.actualizar,  name="actualizar"),
    
    
    path("menu/", views.menu, name="menu"),
    path("crear-anime/", views.crear_anime, name="crear_anime"),
    path("buscar-anime/", views.buscar_anime, name="buscar_anime"),
    path("actualizar-anime/<int:id>/", views.actualizar_anime, name="actualizar_anime"),
    path("eliminar-anime/<int:id>/", views.eliminar_anime, name="eliminar_anime"),

]