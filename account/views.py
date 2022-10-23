from django.shortcuts import render
from .forms import *
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import FormView
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class Create(FormView):
    template_name = 'account/register.html'
    form_class = UserAdminCreationForm
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.save()
        form.instance.user = self.request.user
        return super(Create,self).form_valid(form)
class Home(LoginRequiredMixin,ListView):
    model = User
    context_object_name = 'home'
    template_name = 'account/home.html'

class CustomLogin(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')