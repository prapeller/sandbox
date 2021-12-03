from django.shortcuts import render


def render_template_view(request):
    context_dict = {'name': 'prapeller'}
    return render(request, 'templates_app/first_template.html', context=context_dict)


def render_employee(request):
    context_dict = {'id': 123, 'name': 'Pavel', 'sal': 10000}
    return render(request, 'templates_app/employee.html', context=context_dict)
