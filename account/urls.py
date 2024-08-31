from django.contrib.auth.views import LoginView
from django.urls import path

from account.views import RegistrationView, logout_view, ProfileView

app_name = 'account'

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', logout_view, name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile')
]
