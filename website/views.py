# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Position


def index(request):
    positions = Position.objects.all()
    context = {
        'positions': positions
    }
    return render(request, 'base.html', context)