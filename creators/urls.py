from django.urls import path
from .views import *

urlpatterns = [
    path('posts/', Posts.as_view(), name = 'posts'),
    path('add_post/', AddPost.as_view(), name='add_post'),
    path('update_post/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('delete_post/<int:pk>/', DeletePost.as_view(), name = 'delete_post'),
    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEdit.as_view(), name='profile_edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name = 'add_follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name = 'remove_follower'),

    
]