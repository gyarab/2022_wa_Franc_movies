from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)
    gengere = models.ManyToManyField('Genere', blank=True, null=True)   
    def __str__(self):
        return f"{self.name} ({self.year})"
class Director(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return f"{self.name} ({self.year})"
class Genere(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name