# Copyright (c), 2023-2014, Obafemi Oludahunsi
# @author Obafemi Oludahunsi
# FileName: admin.py
# @version: I
# Creation: 27/08/2023
# Last Modification: 28/08/23

from django.contrib import admin
from .models import Post

# Register your models here.
admin.site.register(Post)
