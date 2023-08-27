# Copyright (c), 2023-2014, Obafemi Oludahunsi
# @author Obafemi Oludahunsi
# FileName: urls.py
# @version: I
# Creation: 27/08/2023
# Last Modification: 28/08/23

from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('post/<str:pk>', views.post, name='post')
]
