from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AnasayfaView(TemplateView):
    template_name='home.html'

class ProfileView(TemplateView):
    template_name='profile.html'

class LoginView(TemplateView):
    template_name='login.html'

class SignupView(TemplateView):
    template_name='signup.html'

class EditView(TemplateView):
    template_name='edit.html'

class FollowersView(TemplateView):
    template_name='followers.html'

class FollowingView(TemplateView):
    template_name='following.html'

class PostsView(TemplateView):
    template_name='posts.html'