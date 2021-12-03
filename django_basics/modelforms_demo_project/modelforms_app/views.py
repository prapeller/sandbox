from django.shortcuts import render
from modelforms_app.forms import ProjectForm
from modelforms_app.models import Project


def index(request):
    context = {'title': 'index page'}
    return render(request, 'modelforms_app/index.html', context)


def project_list(request):
    projects = Project.objects.all()
    context = {
        'title': 'project list',
        'projects': projects,
    }
    return render(request, 'modelforms_app/project-list.html', context)


def project_add(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            form.save()
            return index(request)

    context = {
        'title': 'project add',
        'form': form,
    }
    return render(request, 'modelforms_app/project-add.html', context)
