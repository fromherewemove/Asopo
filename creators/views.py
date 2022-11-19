from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
# Create your views here.
from .models import Post, CreatorFeed
from django.urls import reverse_lazy
from django.views import View

class AddPost(CreateView):
    model = Post
    fields = ['body', 'image']
    template_name = 'creators/addpost.html'
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPost, self).form_valid(form)

class EditPost(UpdateView):
    model = Post
    fields = ['body', 'image']
    template_name = 'creators/addpost.html'
    success_url = reverse_lazy('posts')

class DeletePost(DeleteView):
    model = Post
    template_name = 'creators/deletepost.html'
    success_url = reverse_lazy('posts')
class Posts(ListView):
    model = Post
    template_name = 'creators/posts.html'
    context_object_name = 'posts'
    ordering = ['-created_on']

class ProfileView(View):
    def get(Self, request, pk, *args, **kwargs):
        profile = CreatorFeed.objects.get(pk=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        
        followers = profile.followers.all()
        if len(followers) == 0:
            is_following = False
        for follower in followers:
            if follower == request.user:
                is_following = True
                break
            else:
                is_following = False

        number_of_followers = len(followers)
        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following
        }

        return render(request, 'creators/profile.html', context)

class ProfileEdit(UpdateView):
    model = CreatorFeed
    fields = ['name', 'profileImg', 'services', 'description', 'link', 'link1', 'link2']
    template_name = 'creators/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.user == profile.user

class AddFollower(View):
    def post(self, request, pk, *args, **kwargs):
        profile = CreatorFeed.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)

class RemoveFollower(View):
    def post(self, request, pk, *args, **kwargs):
        profile = CreatorFeed.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)