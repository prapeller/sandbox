from django import forms


class ItemForm(forms.Form):
    name = forms.CharField()
    qty = forms.IntegerField()
