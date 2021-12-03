"""Модуль, содержащий контроллеры веб-приложения"""
from simba_framework.templator import render


class Index:
    def __call__(self):
        return '200 OK', render('index.html')


class About:
    def __call__(self):
        return '200 OK', 'about'


class Contacts:
    def __call__(self):
        return '200 OK', render('contacts.html')