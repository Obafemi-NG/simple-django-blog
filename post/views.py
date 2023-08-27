# Copyright (c), 2023-2014, Obafemi Oludahunsi
# @author Obafemi Oludahunsi
# FileName: views.py
# @version: I
# Creation: 27/08/2023
# Last Modification: 28/08/23


from django.shortcuts import render
from .models import Post

# Create your views here.


def posts(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post': post})
