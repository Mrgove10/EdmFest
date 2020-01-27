from django import forms

from .models import Artist, Festival

class ArtistAddForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ('contry_origin', 'stage_name',)
        
        
class FestivalAddForm(forms.ModelForm):
    class Meta:
        model = Festival
        fields = ('name', 'description',)