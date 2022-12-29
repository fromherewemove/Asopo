from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from creators.models import *
from account.models import User
from django.views import View
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *

class PostsEndUser(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'enduser/posts.html'
    context_object_name = 'posts'
    ordering = ['-created_on']

class ProfileView(LoginRequiredMixin,View):
    def get(Self, request, pk, *args, **kwargs):
        profile = EnduserFeed.objects.get(pk=pk)
        user = profile.user
        
        context = {
            'user': user,
            'profile': profile,
        }

        return render(request, 'enduser/profile.html', context)

class ProfileEdit(LoginRequiredMixin,UpdateView):
    model = EnduserFeed
    fields = ['profileImg']
    template_name = 'enduser/profile_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})
    
    def test_func(self):
        profile = self.get_object()
        return self.user == profile.user


class ListThreads(View):
    def get(self, request, *args, **kwargs):
        threads = Thread.objects.filter(Q(user=request.user) | Q(receiver=request.user))

        context = {
            'threads': threads
        }
        return render(request, 'enduser/inbox.html', context)


class CreateThread(View):
    def get(self, request, *args, **kwargs):
        form = ThreadForm()
        context = {
            'form': form
        }
        return render(request, 'enduser/create_thread.html', context)

    def post(self, request, *args, **kwargs):
        form = ThreadForm(request.POST)

        email = request.POST.get('email')

        try:
            receiver = User.objects.get(email=email)
            if Thread.objects.filter(user=request.user, receiver=receiver).exists():
                thread = Thread.objects.filter(user=request.user, receiver=receiver)[0]
                return redirect('thread', pk=thread.pk)
            elif Thread.objects.filter(user=receiver, receiver=request.user).exists():
                thread = Thread.objects.filter(user=receiver, receiver=request.user)[0]
                return redirect('thread', pk=thread.pk)

            if form.is_valid():
                thread = Thread(
                    user= request.user,
                    receiver=receiver
                )
                thread.save()

                return redirect('thread', pk=thread.pk)
            
    
        except:
            messages.error(request, "Invalid Email")
            return redirect('create_thread')



class ThreadView(View):
    def get(self, request, pk, *args, **kwargs):
        form = MessageForm()
        thread = Thread.objects.get(pk=pk)
        message_list = Message.objects.filter(thread__pk__contains=pk)
        context = {
            'thread': thread,
            'form': form,
            'message_list': message_list
        }
        return render(request, 'enduser/thread.html', context)
   

class CreateMessage(View):
    def post(self, request, pk, *args, **kwargs):
        form = MessageForm(request.POST, request.FILES)
        thread = Thread.objects.get(pk=pk)
        if thread.receiver == request.user:
            receiver = thread.user
        else:
            receiver = thread.receiver

        if form.is_valid():
            message = form.save(commit=False)
            message.thread = thread
            message.sender_user = request.user
            message.receiver_user = receiver
            message.save()
        

        return redirect('thread', pk=pk)