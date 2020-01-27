from django import forms

from .models import Artist, Festival


class ArtistAddForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('stage_name',
                  'first_name',
                  'description', )


class FestivalAddForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ('name',
                  'description',
                  'last_year',)
