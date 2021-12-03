"""fbv_crud_demo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from fbv_crud_app.views import student_list, student_update, student_add, student_delete, card_update

app_name = 'students'

urlpatterns = [
    path('add/', student_add, name='add'),
    path('list/', student_list, name='list'),
    path('update/<int:pk>/', student_update, name='update'),
    path('delete/<int:pk>/', student_delete, name='delete'),
    path('card_update/<int:pk>/', card_update, name='card_update'),
]
