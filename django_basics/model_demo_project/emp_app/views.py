from django.shortcuts import render

from emp_app.models import Employee


def emp_data(request):
    employees = Employee.objects.all()
    context = {'employees': employees}
    return render(request, 'emp_app/employees.html', context=context)