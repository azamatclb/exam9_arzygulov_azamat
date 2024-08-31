from django import forms

from webapp.models import Picture, Album


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ['image', 'summary', 'album', 'is_public']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['album'].queryset = Album.objects.filter(author=user)
