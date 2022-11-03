from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import CreatorFeed, CreatorPost
# Create your views here.
from django.views.generic import FormView

from django.urls import reverse_lazy
class Posts(ListView):
    model = CreatorPost
    context_object_name = 'posts'
    template_name = 'creators/post.html'

class AddPost(CreateView):
    model = CreatorPost
    fields = ('image', 'desc', 'link')
    context_object_name = 'add_post'
    template_name = 'creators/addpost.html'
    success_url = reverse_lazy('posts')