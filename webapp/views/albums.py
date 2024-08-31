from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from webapp.models import Album, Picture
from webapp.forms import AlbumForm


class AlbumDetailView(ListView):
    model = Picture
    template_name = 'album_templates/album_detail.html'
    context_object_name = 'pictures'
    paginate_by = 10

    def get_queryset(self):
        album = get_object_or_404(Album, pk=self.kwargs['pk'])
        return Picture.objects.filter(album=album, is_public=True).order_by('-date_created')


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_templates/album_add.html'
    success_url = reverse_lazy('webapp:albums')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class AlbumUpdateView(LoginRequiredMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_templates/album_add.html'
    success_url = reverse_lazy('webapp:albums')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.pictures.update(is_public=self.object.is_public)
        return response


class AlbumDeleteView(LoginRequiredMixin, DeleteView):
    model = Album
    template_name = 'album_templates/album_delete.html'
    success_url = reverse_lazy('webapp:albums')

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        album.pictures.all().delete()
        return super().delete(request, *args, **kwargs)
