from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('webapp:pictures')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PictureDeleteView(LoginRequiredMixin, DeleteView):
    model = Picture
    template_name = 'picture_templates/picture_delete.html'
    success_url = reverse_lazy('webapp:pictures')


class PictureUpdateView(LoginRequiredMixin, UpdateView):
    model = Picture
    form_class = PictureForm
    template_name = 'picture_templates/picture_add.html'
    success_url = reverse_lazy('webapp:pictures')


class PictureDetailView(LoginRequiredMixin, DetailView):
    model = Picture
    template_name = 'picture_templates/picture_detail.html'
    context_object_name = 'picture'
