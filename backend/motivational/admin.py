# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Quote, ImageAddress

# Register your models here.

admin.site.register(Quote)
admin.site.register(ImageAddress)