from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # artists
    path('artists/', views.artists, name='artists'),
    path('artist/<int:id>/', views.artist, name='artist'),
    path('artist/add/', views.artistAdd, name='artistAdd'),
    # festivals
    path('festivals/', views.festivals, name='festivals'),
    path('festival/<int:id>/', views.festival, name='festival'),
    path('festival/add/', views.festivalAdd, name='festivalAdd'),
]
