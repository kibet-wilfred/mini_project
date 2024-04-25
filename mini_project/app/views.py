from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

def registration(request):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render)


