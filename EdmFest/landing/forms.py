from django import forms

from .models import Artist, Festival


class ArtistAddForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('stage_name',
                  'first_name',
                  'description',
                  'born',
                  'contry_origin',
                  'died',
                  'is_active',
                  'last_name')


class FestivalAddForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ('name',
                  'description',
                  'last_year',
                  'contry',
                  'first_year',
                  'headliners',
                  'location_lat',
                  'location_lng',
                  'location_name',
                  'youtube_chanel')
