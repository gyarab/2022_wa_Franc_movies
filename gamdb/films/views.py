from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Director, Actor, Genere

# Create your views here.
def homepage(request):
    context = {
        'movies': Movie.objects.all(),
        'actors': Actor.objects.all(),
        'directors': Director.objects.all(),
        'generes': Genere.objects.all()
    }
    return render(request, 'homepage.html', context)
def movies(request):
    movie_querrystring = Movie.objects.all()

    genre = request.GET.get('genre')
    if genre:
        movie_querrystring = movie_querrystring.filter(gengere__name=genre)
    search = request.GET.get('search')
    if search:
        movie_querrystring = movie_querrystring.filter(name__icontains=search)
    context = {
        'movies': movie_querrystring,
        'genres': Genere.objects.all(),
        'genre' : genre,
        'search': search,
    }
    return render(request, 'movies.html', context)
def movie(request, id):
    context = {
        "movie" : Movie.objects.get(id=id),
    }
    return render(request,'movie.html', context)
def directors(request):
    context = {
        'title' : "Režizéři",
        'directors': Director.objects.all(),
    }
    return render(request, 'directors.html', context)
def director(request, id):
    context = {
        "director" : Director.objects.get(id=id),
    }
    return render(request, 'director.html', context)
def actors(request):
    context = {
        'actors': Actor.objects.all(),
    }
    return render(request, 'actors.html', context)
def actor(request, id):
    context = {
        "actor" : Actor.objects.get(id=id),
    }
    return render(request, 'actor.html', context)

    #return HttpResponse("<h1>Ahoj</h1>")