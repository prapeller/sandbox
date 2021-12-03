from django.shortcuts import render
from django.http import HttpResponse


def display_quote(request):
    return HttpResponse('the best investment we can make to ourselve!')
