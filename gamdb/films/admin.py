from django.contrib import admin
from .models import Movie, Genere, Comment, Person

# Register your models here.
admin.site.register(Movie)
admin.site.register(Person)
admin.site.register(Genere)
admin.site.register(Comment)