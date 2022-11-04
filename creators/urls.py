from django.urls import path
from .views import Posts, AddPost, DeletePost, UpdatePost
urlpatterns = [
    path('', Posts.as_view(), name='post'),
    path('add_post/', AddPost.as_view(), name = 'add_post'),
    path('delete_post/<int:pk>/', DeletePost.as_view(), name='delete_post'),
    path('update_post/<int:pk>/', UpdatePost.as_view(), name='update_post')
]