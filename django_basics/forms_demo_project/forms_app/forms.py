import re

from django import forms
from django.core import validators


class UserRegistrationForm(forms.Form):
    MALE = 'Male'
    FEMALE = 'Female'
    GENDERS = [('m', MALE), ('f', FEMALE)]

    first_name = forms.CharField(widget=forms.TextInput,
                                 validators=[
                                     validators.MinLengthValidator(5),
                                     validators.MaxLengthValidator(25),
                                 ])
    last_name = forms.CharField(widget=forms.TextInput, required=False)
    email = forms.CharField(widget=forms.EmailInput,
                            validators=[
                                # validators.RegexValidator(regex=r'.*\.(com|COM)$', message='there should be .com in the end'),
                                validators.RegexValidator(r'.*\.(ru|RU)$', 'there should not be .ru in the end', inverse_match=True),
                            ])
    gender = forms.CharField(widget=forms.Select(choices=GENDERS))
    password = forms.CharField(widget=forms.PasswordInput)
    ssn = forms.IntegerField()

    # def clean_first_name(self):
    #     input_first_name = self.cleaned_data.get('first_name')
    #     if len(input_first_name) > 10:
    #         raise forms.ValidationError('The max length of first_name is 10 characters')
    #     return  input_first_name
    #
    # def clean_email(self):
    #     input_email = self.cleaned_data.get('email')
    #     if '@mail.ru' in input_email:
    #         raise forms.ValidationError('we dont trust mail.ru services!))))')
    #     return input_email

    # def clean(self):
    #     cleaned_data = super().clean()
    #     input_first_name = cleaned_data.get('first_name')
    #     input_email = cleaned_data.get('email')
    #
    #     if len(input_first_name) > 10:
    #         raise forms.ValidationError('The max length of first_name is 10 characters')
    #     if '@mail.ru' in input_email:
    #         raise forms.ValidationError('we dont trust mail.ru services!))))')
    #
    #     return cleaned_data
