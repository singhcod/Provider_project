from django import forms
from Employee.models import Employees

class Employee_ModelForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'