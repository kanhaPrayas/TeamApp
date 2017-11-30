# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Team

# Register your models here.


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'phone')
    ordering = ('role', 'age')
