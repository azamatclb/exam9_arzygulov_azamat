from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from webapp.forms.picture import PictureForm
from webapp.models import Picture


# Create your views here.

class PictureListView(ListView):
    model = Picture
    template_name = 'picture_templates/pictures.html'
    context_object_name = 'pictures'
    paginate_by = 10

    def get_queryset(self):
        return Picture.objects.filter(is_public=True).order_by('-date_created')


class PictureAddView(LoginRequiredMixin, CreateView):
    model = Picture
    form_class = PictureForm
    template_name = 'picture_templates/picture_add.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        kwargs['album_id'] = self.request.GET.get('album')
        return kwargs

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:pictures')


class PictureDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Picture
    template_name = 'picture_templates/picture_delete.html'
    success_url = reverse_lazy('webapp:pictures')

    def test_func(self):
        picture = self.get_object()
        return self.request.user == picture.author or self.request.user.has_perm('webapp:delete_pictures')


class PictureUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Picture
    form_class = PictureForm
    template_name = 'picture_templates/picture_add.html'
    success_url = reverse_lazy('webapp:pictures')

    def test_func(self):
        picture = self.get_object()
        return self.request.user == picture.author or self.request.user.has_perm('webapp:update_picture')


class PictureDetailView(LoginRequiredMixin, DetailView):
    model = Picture
    template_name = 'picture_templates/picture_detail.html'
    context_object_name = 'picture'
