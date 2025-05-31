from django.shortcuts import render
from .models import Post
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView


class HomeListVeiw(ListView):
    model = Post
    template_name = 'home.html'

class AloqaListVeiw(ListView):
    model = Post
    template_name = 'aloqa.html'


class PostDetailVeiw(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title' , 'body']