from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('artist/<int:id>',views.artist, name='artist'),
    path('festival/<int:id>',views.festival, name='festival'),
]
