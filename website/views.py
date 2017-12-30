# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Position, Education


def index(request):
    positions = Position.objects.all()
    educations = Education.objects.all()
    context = {
        'positions': positions,
        'educations': educations,
    }
    return render(request, 'base.html', context)


def imprint(request):
    return render(request, 'imprint.html')