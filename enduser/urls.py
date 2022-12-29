from django.urls import path
from .views import *

urlpatterns = [   
    path('posts/', PostsEndUser.as_view(), name = 'creator_posts'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user_profile'),
    path('profile/edit/<int:pk>/', ProfileEdit.as_view(), name='user_profile_edit'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('inbox/create_thread/', CreateThread.as_view(), name='create_thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create_message', CreateMessage.as_view(), name = 'create_message')
]