from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView

from account.form import UserRegistrationForm
from webapp.models import Picture, Album

# Create your views here.

User = get_user_model()


class RegistrationView(CreateView):
    template_name = 'registration.html'
    form_class = UserRegistrationForm
    model = User

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if not next_url:
            next_url = self.request.POST.get('next')
        if not next_url:
            next_url = reverse('webapp:pictures')
        return next_url


def logout_view(request):
    logout(request)
    return redirect('webapp:pictures')


class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        if self.request.user == user:
            context['pictures'] = Picture.objects.filter(author=user).order_by('-date_created')
        else:
            context['pictures'] = Picture.objects.filter(author=user, is_public=True).order_by('-date_created')
        context['albums'] = Album.objects.filter(author=user)
        return context
