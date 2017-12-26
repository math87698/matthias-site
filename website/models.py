# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Position(models.Model):
    company = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=150)


class Education(models.Model):
    facility = models.CharField(max_length=70)
    city = models.CharField(max_length=70)
    country = models.CharField(max_length=70)
    date_from = models.DateField()
    date_to = models.DateField()
    degree = models.CharField(max_length=70)