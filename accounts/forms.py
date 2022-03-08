from django import forms
from django.forms import ModelForm
from .models import *
class AddEmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields=['name','empcode','city','desig','pic']