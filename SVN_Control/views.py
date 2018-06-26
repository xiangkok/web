from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader


# Create your views here.

def model(request):
    return render(request, 'SVN_Control/model.html')


def tag(request):
    return render(request, 'SVN_Control/tag.html')


def platform(request):
    return render(request, 'SVN_Control/platform.html')


def search(request):
    return render(request, 'SVN_Control/search.html')


def index(request):
    return render(request, 'SVN_Control/index.html')
