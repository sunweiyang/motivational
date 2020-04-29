# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Quote(models.Model):
    text = models.TextField()
    author = models.TextField()


class ImageAddress(models.Model):
    url = models.TextField()
