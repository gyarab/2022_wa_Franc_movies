"""gamdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from films.views import homepage, directors, movie, movies, director, actor, actors

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name="home"),
    path('movies/', movies, name="movies"),
    path('movie/<int:id>', movie, name="movie"),
    path('directors/', directors, name="directors"),
    path('director/<slug:slug>/', director, name="director"),
    path('actors/', actors, name="actors"),
    path('actor/<slug:slug>', actor, name="actor"),
]
