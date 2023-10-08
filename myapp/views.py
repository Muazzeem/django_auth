from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm

from django.http import HttpResponse

from .models import CustomUser


class CustomUserCreateView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class CustomUserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')


class UserDetailView(LoginRequiredMixin, DetailView):
    model = CustomUser  # Replace with your custom user model
    template_name = 'user_detail.html'
    context_object_name = 'user'  # This is the name you'll use in the template to access the user object

    def get_object(self, queryset=None):
        return self.request.user  # Retrieve the currently logged-in user


class CustomUserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
