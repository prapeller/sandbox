from django.shortcuts import render
from .forms import UserRegistrationForm


def user_registration_view(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            print('form is valid')
            print(f'first_name value: {form.cleaned_data.get("first_name")}')
            print(f'last_name value: {form.cleaned_data.get("last_name")}')
            print(f'email value: {form.cleaned_data.get("email")}')
            print(f'gender value: {form.cleaned_data.get("gender")}')
            print(f'password value: {form.cleaned_data.get("password")}')
            print(f'ssn value: {form.cleaned_data.get("ssn")}')

    context = {'form': form}

    return render(request, 'forms_app/forms.html', context=context)
