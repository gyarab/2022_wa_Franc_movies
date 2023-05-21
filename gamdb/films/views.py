from django.shortcuts import render
from django.db.models import Count
from django.http import HttpResponse
from .models import Movie, Genere, Comment, Person
from django.db.models import Q
from .forms import CommentForm

# Create your views here.
def homepage(request):
    context = {
        'bestMovies': Movie.objects.all().exclude(rating__isnull=True).order_by('-rating')[:3],
        'worstMovies': Movie.objects.all().exclude(rating__isnull=True).order_by('rating')[:3],
        'actors':Person.objects.annotate(num_connections=Count('acted')).filter(num_connections__gt=0),
        'directors': Person.objects.annotate(num_connections=Count('directed')).filter(num_connections__gt=0),
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
        'search': search,    }
    return render(request, 'movies.html', context)
def movie(request, id):
    m = Movie.objects.get(id=id)
    f = CommentForm()

    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            # ulozit do DB
            c = Comment(
                movie=m,
                author=f.cleaned_data.get('author'),
                text=f.cleaned_data.get('text'),
                rating=f.cleaned_data.get('rating'),
            )
            if not c.author:
                c.author = 'Anonym'
            c.save()
            # Přidej statistiku do filmu
            if f.cleaned_data.get('rating') == 'T':
                m.potato += 1
            if f.cleaned_data.get('rating') == 'F':
                m.frie += 1
            m.rating = 100 * m.frie/(m.frie+m.potato)
            m.save()
            # nastavit prazdny form
            f = CommentForm()

    context = {
        "movie": m,
        "comments": Comment.objects.filter(movie=m).order_by('-created_at'),
        "form": f
    }
    return render(request,'movie.html', context)
def directors(request):
    context = {
        'title' : "director",
        'type' : "directors",
        'persons': Person.objects.annotate(num_connections=Count('directed')).filter(num_connections__gt=0),
    }
    return render(request, 'persons.html', context)
def director(request, slug):
    context = {
        "person" : Person.objects.get(slug=slug),
        type: "director"
    }
    return render(request, 'person.html', context)
def actors(request):
    context = {
        'title' : "actor",
        'type' : "actors",
        'persons': Person.objects.annotate(num_connections=Count('acted')).filter(num_connections__gt=0),
    }
    return render(request, 'persons.html', context)
def actor(request, slug):
    context = {
        "person" : Person.objects.get(slug=slug),
    }
    return render(request, 'person.html', context)
    #return HttpResponse("<h1>Ahoj</h1>")