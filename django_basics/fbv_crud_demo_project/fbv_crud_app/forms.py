from django import forms
from fbv_crud_app.models import Student, StudentCard


class StudentForm(forms.ModelForm):
    headman = forms.ModelChoiceField(Student.objects, label='headman', required=False)

    class Meta:
        model = Student
        fields = '__all__'


class StudentCardForm(forms.ModelForm):
    class Meta:
        model = StudentCard
        fields = '__all__'
