from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Practica, Anime

# Vista de registro 
def formulario(request):
    if request.method == "POST":
        usern = request.POST.get("username")
        passw1 = request.POST.get("password1")
        passw2 = request.POST.get("password2")
        imagen_url = request.POST.get("imagen")

        if Practica.objects.filter(username=usern).exists():
            sms = "El nombre de usuario ya existe"
            sms2 = "Segundo mensaje"
            info = {
                  'infosms':sms,
                  'infosms2':sms2
            }
            return render(request, "formulario.html", info)
        # Validación básica
        if passw1 == passw2:
            # Guardar en la base de datos
            Practica.objects.create(
                username=usern,
                password=passw2,
                imagen=imagen_url
            )
            return redirect("login")
    return render(request, "formulario.html")


# Vista de login
def login(request):
    if request.method == "POST":
        usern = request.POST.get("username")
        passw = request.POST.get("password")
        
        try:
            usuario = Practica.objects.get(username=usern)
            # Verificar la contraseña
            if usuario.password == passw:
                # Login exitoso
                return redirect("menu")
            else:
                sms = "Contraseña incorrecta"
                sms2 = "Intenta de nuevo"
                info = {
                    'infosms': sms,
                    'infosms2': sms2
                }
                return render(request, "login.html", info)
        except Practica.DoesNotExist:
            sms = "El usuario no existe"
            sms2 = "Verifica tu nombre de usuario"
            info = {
                'infosms': sms,
                'infosms2': sms2
            }
            return render(request, "login.html", info)
    
    return render(request, "login.html")


# Vista del menú principal con animes
def menu(request):
    animes = Anime.objects.all()
    context = {
        'animes': animes
    }
    return render(request, 'menu.html', context)



#  Crear anime
def crear_anime(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        descripcion = request.POST.get("descripcion")
        imagen = request.POST.get("imagen")
        episodios = request.POST.get("episodios")
        calidad = request.POST.get("calidad")
        genero = request.POST.get("genero")
        rating = request.POST.get("rating")
        
        Anime.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            imagen=imagen,
            episodios=episodios,
            calidad=calidad,
            genero=genero,
            rating=rating
        )
        return redirect("menu")
    
    return render(request, "crear_anime.html")


#  Buscar anime
def buscar_anime(request):
    query = request.GET.get("q", "")
    if query:
        animes = Anime.objects.filter(nombre__icontains=query)
    else:
        animes = Anime.objects.all()
    
    context = {
        'animes': animes,
        'query': query
    }
    return render(request, "buscar_anime.html", context)


# Actualizar anime
def actualizar_anime(request, id):
    anime = Anime.objects.get(id=id)
    
    if request.method == "POST":
        anime.nombre = request.POST.get("nombre")
        anime.descripcion = request.POST.get("descripcion")
        anime.imagen = request.POST.get("imagen")
        anime.episodios = request.POST.get("episodios")
        anime.calidad = request.POST.get("calidad")
        anime.genero = request.POST.get("genero")
        anime.rating = request.POST.get("rating")
        
        anime.save()
        
        sms = "Anime actualizado correctamente"
        info = {
            'infosms': sms,
            'anime': anime
        }
        return render(request, "actualizar_anime.html", info)
    
    context = {
        'anime': anime
    }
    return render(request, "actualizar_anime.html", context)


# Eliminar anime
def eliminar_anime(request, id):
    anime = Anime.objects.get(id=id)
    
    if request.method == "POST":
        anime.delete()
        return redirect("menu")
    
    context = {
        'anime': anime
    }
    return render(request, "eliminar_anime.html", context)



def Vista1(request):
    return render(request, 'vista.html')


def Vista2(request):
    return render(request, 'vista2.html')


def usuarios(request):
    todos_usuarios = Practica.objects.all()
    context = {
        'usuarios': todos_usuarios
    }
    return render(request, 'usuarios.html', context)


def actualizar(request, id):
    usuario = Practica.objects.get(id=id)
    
    if request.method == "POST":
        nuevo_username = request.POST.get("username")
        nueva_password = request.POST.get("password")
        nueva_imagen = request.POST.get("imagen")
        
        usuario.username = nuevo_username
        
        if nueva_password:
            usuario.password = nueva_password
        
        usuario.imagen = nueva_imagen
        
        usuario.save()
        
        sms = "Datos actualizados correctamente"
        info = {
            'infosms': sms,
            'usuario': usuario
        }
        return render(request, "actualizar.html", info)
    
    context = {
        'usuario': usuario
    }
    return render(request, "actualizar.html", context)