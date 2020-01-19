from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Festival, Artist
# Create your views here.


def index(request):
    template = loader.get_template('landing/index.html')
    context = {}  # to passe variables in teh view
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