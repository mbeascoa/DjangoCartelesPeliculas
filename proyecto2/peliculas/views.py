from django.shortcuts import render
from peliculas.models import Pelicula


def index(request):
    peli = Pelicula()
    cursor=peli.devolverdato()
    contexto = {
        'listado_peliculas': cursor
    }
    return render(request, "peliculas/mispeliculas.html", contexto)