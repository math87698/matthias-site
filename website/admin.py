# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Position, Education


class PositionAdmin(admin.ModelAdmin):
    list_display = ('company','city','country','date_from','date_to','title')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('facility', 'city', 'country', 'date_from', 'date_to', 'degree')


admin.site.register(Position, PositionAdmin)
admin.site.register(Education, EducationAdmin)