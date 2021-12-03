from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator

from clinicals_app.forms import ClinicalDataForm, PatientForm
from clinicals_app.models import Patient, ClinicalData


def index(request):
    context = {
        'title': 'Clinicals'
    }
    return render(request, 'index.html', context)


@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_staff), name='dispatch')
class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('patients:list')
    fields = ('first_name', 'last_name', 'age')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create patient'
        return context


@method_decorator(user_passes_test(lambda u: u.is_authenticated), name='dispatch')
class PatientListView(ListView):
    model = Patient

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List patients'
        return context


@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_staff), name='dispatch')
class PatientUpdateView(UpdateView):
    model = Patient
    fields = ('first_name', 'last_name', 'age')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update patient'
        return context

    def post(self, request, *args, **kwargs):
        patient = self.get_object()
        form = PatientForm(data=self.request.POST, instance=patient)

        if form.is_valid():
            form.save()
            messages.success(self.request, 'Success! Patient data was updated!')
            return redirect(self.request.META['HTTP_REFERER'])
        else:
            messages.error(self.request, 'recheck fields')
            return redirect(self.request.META['HTTP_REFERER'])


@method_decorator(user_passes_test(lambda u: u.is_authenticated and u.is_superuser),
                  name='dispatch')
class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patients:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete patient'
        return context


@login_required
def add_data(request, pk):
    patient = Patient.objects.get(pk=pk)
    clinical_data = ClinicalData(patient=patient)
    clinical_data_form = ClinicalDataForm(instance=clinical_data)
    if request.method == 'POST':
        clinical_data_form = ClinicalDataForm(data=request.POST)
        clinical_data_form.save()
        return redirect('patients:list')

    context = {
        'title': 'Add data',
        'patient': patient,
        'clinical_data_form': clinical_data_form,
    }
    return render(request, 'clinicals_app/patient_add_data.html', context)


@login_required
def analyze(request, pk):
    patient = Patient.objects.get(pk=pk)
    clinical_data = ClinicalData.objects.filter(patient=patient)

    hr_measured = clinical_data.filter(name='hr')
    last_hr = clinical_data.filter(name='hr').order_by(
        '-measured_time').first().value if hr_measured else 'Not measured yet'

    hw_measured = clinical_data.filter(name='hw')
    last_hw = clinical_data.filter(name='hw').order_by(
        '-measured_time').first().value if hw_measured else 'Not measured yet'

    bp_measured = clinical_data.filter(name='bp')
    last_bp = clinical_data.filter(name='bp').order_by(
        '-measured_time').first().value if bp_measured else 'Not measured yet'

    context = {
        'title': 'Patient analyze',
        'patient': patient,
        'clinical_data': clinical_data,
        'last_hr': last_hr,
        'last_hw': last_hw,
        'last_bp': last_bp,
    }
    return render(request, 'clinicals_app/patient_analyze.html', context)
