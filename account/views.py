from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from account.form import UserRegistrationForm

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


class ProfileView(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'user_obj'

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs['pk'])
