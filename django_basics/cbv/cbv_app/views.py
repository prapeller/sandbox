from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class HelloView(View):

    hello = '<h1>HELLO!!!</h1>'

    def get(self, request):
        return HttpResponse(self.hello)
