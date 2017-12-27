# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
#from .models import Position


def index(request):
    # position = get_object_or_404(Position)
    # context = {
    #     'position': position
    # }
    return render(request, 'base.html')