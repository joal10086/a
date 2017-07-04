'''
Created on 3 Jul 2017

@author: it
'''

from django.http import HttpResponse
 
def base(request):
    return render(request, 'base.html')


# -*- coding: utf-8 -*-
 
#from django.http import HttpResponse
from django.shortcuts import render
import os

def hello(request):
    #return HttpResponse("Hello world 111! ")
    print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)