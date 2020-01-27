from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Festival, Artist

from .forms import FestivalAddForm, ArtistAddForm
# Create your views here.


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}  # to passe variables in teh view
    return HttpResponse(template.render(context, request))

def artists(request):
    template = loader.get_template('landing/artists.html')
    context = {
        "artists": Artist.objects.all()
    }
    return HttpResponse(template.render(context, request))


def artist(request, id):
    try:
        artistVar = Artist.objects.get(pk=id)
    except Artist.DoesNotExist:
        raise Http404
    template = loader.get_template('landing/artist.html')
    context = {
        "artist": artistVar
    }
    return HttpResponse(template.render(context, request))


def festivals(request):
    template = loader.get_template('landing/festivals.html')
    context = {
        "festivals": Festival.objects.all()
    }
    return HttpResponse(template.render(context, request))


def festival(request, id):
    try:
        festivalVar = Festival.objects.get(pk=id)
    except Festival.DoesNotExist:
        raise Http404
    template = loader.get_template('landing/festival.html')
    context = {
        "festival": festivalVar
    }
    return HttpResponse(template.render(context, request))

#https://tutorial.djangogirls.org/en/django_forms/

def festivalAdd(request):
    form = FestivalAddForm()
    return render(request, 'landing/festivalAdd.html', {'form': form})


def artistAdd(request):
    form = ArtistAddForm()
    return render(request, 'landing/artistadd.html', {'form': form})
