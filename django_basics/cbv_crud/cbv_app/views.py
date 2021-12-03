from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from cbv_app.models import Student


def index(request):
    return render(request, 'cbv_app/index.html')


class Create(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'test_score')
    # template_name = 'student_form.html'


class List(ListView):
    model = Student
    # template_name = 'student_list.html'
    # context_object_name = 'student_list'


class Detail(DetailView):
    model = Student
    # template_name = 'student_detail.html'
    # context_object_name = 'student'


class Update(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'test_score')
    # template_name = 'student_form.html'


class Delete(DeleteView):
    model = Student
    success_url = reverse_lazy('students:list')
    # template_name = 'student_confirm_delete.html'
    # context_object_name = 'student'
