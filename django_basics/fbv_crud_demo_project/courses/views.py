from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from courses.forms import CourseForm
from courses.models import Course


@login_required
def course_list(request):
    courses = Course.objects.all().order_by('pk')
    context = {
        'title': 'Courses list',
        'courses': courses,
    }
    return render(request, 'courses/course-list.html', context)


@login_required
def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            if 'update_and_to_list' in request.POST:
                return redirect('/courses/list/')

    context = {
        'title': 'Student update',
        'course': course,
        'form': form,
    }
    return render(request, 'courses/course-update.html', context)


@login_required
def course_add(request):
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/courses/list/')

    context = {
        'title': 'Course Add',
        'form': form,
    }
    return render(request, 'courses/course-add.html', context)


@login_required
def course_delete(request, pk):
    Course.objects.get(pk=pk).delete()
    return redirect(request.META.get('HTTP_REFERER'))
