# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import ContactInfo, HomeContentPictures

admin.site.register(ContactInfo)
admin.site.register(HomeContentPictures)

# Register your models here.
