from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    avg_rating = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)
    director = models.ManyToManyField('Person', blank=True, null=True, related_name='directed')
    actor = models.ManyToManyField('Person', blank=True, null=True, related_name='acted')
    gengere = models.ManyToManyField('Genere', blank=True, null=True)   
    def __str__(self):
        return f"{self.name} ({self.year})"
    def genres_display(self):
        return ", ".join([i.name for i in self.genres.all()])
        # out = ""
        # for i in self.genres.all():
        #     out += f"{i.name}, "
        # return out

class Person(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return f"{self.name} ({self.year})"
class Genere(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # Po smazání filmu odstran i komentar
    author = models.CharField(max_length=255, blank=True)
    text = models.TextField(blank=True)
    rating = models.IntegerField(null=True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)