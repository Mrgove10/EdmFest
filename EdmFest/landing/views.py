from django.shortcuts import render, get_list_or_404, redirect
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
        "festival": festivalVar,
        "headliners":festivalVar.headliners.all(),
    }
    return HttpResponse(template.render(context, request))

#https://tutorial.djangogirls.org/en/django_forms/

def festivalAdd(request):
    if request.method == "POST":
        form = FestivalAddForm(request.POST)
        if form.is_valid():
            festival = form.save(commit=False)
            festival.added_by = request.user
            festival.name = request.POST['name']
            festival.description = request.POST['description']
            festival.last_year = request.POST['last_year']
            festival.contry = request.POST['contry']
            festival.first_year = request.POST['first_year']
            festival.location_lat = request.POST['location_lat']
            festival.location_lng = request.POST['location_lng']
            festival.location_name = request.POST['location_name']
            festival.youtube_chanel = request.POST['youtube_chanel']
            festival.save()
            festival.headliners.set(request.POST['headliners'])
            festival.save()
            return redirect('festival', id=festival.id)
    else:
        form = FestivalAddForm()
    return render(request, 'landing/festivalAdd.html', {'form': form})


def artistAdd(request):
    if request.method == "POST":
        form = ArtistAddForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.added_by = request.user
            artist.stage_name = request.POST['stage_name']
            artist.first_name = request.POST['first_name']
            artist.description = request.POST['description']
            artist.born = request.POST['born']
            artist.contry_origin = request.POST['contry_origin']
            artist.died = request.POST['died']
            if request.POST['is_active'] == 'true':
                artist.is_active = True
            else:
                artist.is_active = False
            artist.last_name = request.POST['last_name']
            artist.save()
            return redirect('artist', id=artist.id)
    else:
        form = ArtistAddForm()           
    return render(request, 'landing/artistadd.html', {'form': form})
