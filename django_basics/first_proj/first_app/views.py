from django.shortcuts import render
from django.http import HttpResponse
import datetime


def display(request):
    return HttpResponse("<h1>hello!</h1>")


def display_datetime(request):
    now = datetime.datetime.now()
    s = f'<h1>current time: {now}</h1>'
    return HttpResponse(s)
