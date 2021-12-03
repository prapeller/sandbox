from django.shortcuts import render

# JsonResponse - serializer
from django.http import JsonResponse
from core import models
from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
def employee_view(requests):
    """fbv returning serialized employee restful endpoint"""
    emp = {
        'id': 123,
        'name': 'John',
        'salary': 10000000,
    }

    emps_qrst = models.Employee.objects.all()
    emps_lst = list(emps_qrst.values('id','name', 'sal'))
    context = {'employees':emps_lst}

    return JsonResponse(context)
