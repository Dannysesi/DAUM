from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.signup, name='signup'),
    path('create-post', views.create_post, name='create-post'),
]