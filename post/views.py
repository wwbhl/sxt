# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.http import HttpResponse
from django.shortcuts import render
import os

from models import *

# Create your views here.
def index(request):
    map = {'categorys':Category.objects.all(),'title':'Django全栈开发'}
    map['categorys']
    return render(request,'index.html',map)