from django.contrib import admin
from django.urls import path, include
from .views import views, auth
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('blogs', views.blogs, name='blogs'),
    path('logout', auth.logout, name='logout'),
    path('blog-post', views.blog_post, name='blog-post'),

    
    path("login/", auth.login_view, name="login"),
    path("logout/", auth.logout_view, name="logout"),
    path("register/", auth.register, name="register"),
]