from django.shortcuts import render
from django.http import HttpResponse


def first_view(request):
    return HttpResponse('django + docker Volumes are super!')
