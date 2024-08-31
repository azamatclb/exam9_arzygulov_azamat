from django import forms
from webapp.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image', 'summary', 'album']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        album_id = kwargs.pop('album_id', None)
        super().__init__(*args, **kwargs)
        if album_id:
            self.fields['album'].initial = album_id
