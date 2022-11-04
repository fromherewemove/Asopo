from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
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

    def form_valid(self, form):
        
        form.instance.author = self.request.user
        return super(AddPost, self).form_valid(form)

class DeletePost(DeleteView):
    model = CreatorPost
    context_object_name = 'delete_post'
    success_url = reverse_lazy('posts')
    template_name = 'creators/deletepost.html'

class UpdatePost(UpdateView):
    model = CreatorPost
    fields = ('image', 'desc', 'link')
    success_url = reverse_lazy('posts')
    template_name = 'creators/addpost.html'
    

