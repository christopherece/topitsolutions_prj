from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),  # Home page, lists all posts
    path('post/<slug:slug>/', views.blog_detail, name='blog_detail'),  # View a single post
    path('post/new/', views.blog_create, name='blog_create'),  # Create a new post
    path('post/edit/<slug:slug>/', views.blog_edit, name='blog_edit'),  # Edit an existing post
]