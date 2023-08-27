# Copyright (c), 2023-2014, Obafemi Oludahunsi
# @author Obafemi Oludahunsi
# FileName: models.py
# @version: I
# Creation: 27/08/2023
# Last Modification: 28/08/23

from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
