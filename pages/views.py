from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from django.contrib.auth.models import User


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class UsersListView(ListView):
    model = User
    template_name = 'users.html'