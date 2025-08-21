# myapp/forms.py
from django import forms
from .models import InputForm

class MyDataForm(forms.ModelForm):
    class Meta:
        model = InputForm
        fields = ['name', 'email', 'roll_number', 'password']