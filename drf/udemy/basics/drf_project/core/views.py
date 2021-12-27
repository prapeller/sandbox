from django.shortcuts import render

# JsonResponse - serializer
from django.http import JsonResponse
from core.models import Employee
from rest_framework.decorators import api_view


# @api_view(['GET', 'POST'])
def employee_view(requests):
    """fbv returning serialized employee restful endpoint"""
    emp = {
        'id': 123,
        'name': 'John',
        'salary': 10000000,
    }

    emps_qrst = Employee.objects.all()
    emps = list(emps_qrst.values('name', 'sal'))
    resp = {'emps': emps}

    return JsonResponse(resp)
