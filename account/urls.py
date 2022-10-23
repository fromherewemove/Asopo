from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [

    path('',  Create.as_view(), name='create' ),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', Home.as_view(), name='home'),
    path('login/', CustomLogin.as_view(), name='login')
]
