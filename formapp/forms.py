from django import forms


class CreateForm(forms.Form):
    name = forms.CharField(label="Name", max_length=200)