from django.contrib import admin
from .models import Movie, Director, Genere, Comment

# Register your models here.
admin.site.register(Movie)
admin.site.register(Director)
admin.site.register(Genere)
admin.site.register(Comment)