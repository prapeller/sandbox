import django.forms
from django.shortcuts import render, redirect

# redirect(url) - redirects to particular url

from fbv_crud_app.forms import StudentForm, StudentCardForm
from fbv_crud_app.models import Student, StudentCard
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required


# if create in auth_permission line with 'view_index' codename
# @permission_required('view_index')
def index(request):
    context = {
        'title': 'FBV Crud Operations Main',
    }
    return render(request, 'fbv_app/index.html', context)


@login_required
def student_add(request):
    form = StudentForm()

    if request.method == 'POST':
        form = StudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/students/list/')

    context = {
        'title': 'Student add',
        'form': form,
    }
    return render(request, 'fbv_app/student-add.html', context)


@login_required
def student_list(request):
    students = Student.objects.all()

    context = {
        'title': 'Student list',
        'students': students,
    }
    return render(request, 'fbv_app/student-list.html', context)


@login_required
@permission_required('fbv_crud_app.change_student')
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    form = StudentForm(instance=student)

    if request.method == 'POST':
        form = StudentForm(data=request.POST, instance=student)
        if form.is_valid():
            form.save()
            if 'update_and_to_list' in request.POST:
                return redirect('/students/list/')

    context = {
        'title': 'Student update',
        'student': student,
        'form': form,
    }
    return render(request, 'fbv_app/student-update.html', context)


def card_update(request, pk):
    card = StudentCard.objects.get(pk=pk)
    form = StudentCardForm(instance=card)
    if request.method == 'POST':
        form = StudentCardForm(instance=card, data=request.POST)
        if form.is_valid():
            form.save()
            if 'update_and_to_list' in request.POST:
                return redirect('/students/list/')

    context = {
        'form': form,
    }
    return render(request, 'fbv_app/card-update.html', context)


@login_required
@permission_required('fbv_crud_app.delete_student')
def student_delete(request, pk):
    Student.objects.get(pk=pk).delete()

    return redirect(request.META.get('HTTP_REFERER'))


def logout(request):
    return render(request, 'fbv_app/logout.html')


