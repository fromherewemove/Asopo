from django.urls import path
from .views import Posts, AddPost
urlpatterns = [
    path('', Posts.as_view(), name='post'),
    path('add_post/', AddPost.as_view(), name = 'add_post') 
]