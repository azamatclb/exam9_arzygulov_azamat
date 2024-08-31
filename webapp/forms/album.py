from django import forms
from webapp.models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'summary', 'is_public']
