from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from webapp.models import Album, Picture
from webapp.forms import AlbumForm

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from webapp.models import Album, Picture


class AlbumDetailView(DetailView):
    model = Album
    template_name = 'album_templates/album_detail.html'
    context_object_name = 'album'
    paginate_by = 10

    def get_queryset(self):
        return Album.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album = self.get_object()
        context['pictures'] = Picture.objects.filter(album=album, is_public=True).order_by('-date_created')
        return context


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_templates/album_add.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:album_detail', kwargs={'pk': self.object.pk})


class AlbumUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'album_templates/album_add.html'
    success_url = reverse_lazy('webapp:albums')

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.pictures.update(is_public=self.object.is_public)
        return response

    def test_func(self):
        picture = self.get_object()
        return self.request.user == picture.author or self.request.user.has_perm('webapp:update_picture')


class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'album_templates/album_delete.html'
    success_url = reverse_lazy('webapp:albums')

    def delete(self, request, *args, **kwargs):
        album = self.get_object()
        album.pictures.all().delete()
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        picture = self.get_object()
        return self.request.user == picture.author or self.request.user.has_perm('webapp:update_picture')
