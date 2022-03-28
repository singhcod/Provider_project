from django.shortcuts import render
from Employee.models import Employees
from Employee.forms import Employee_ModelForm

from django.views.generic import (ListView,DetailView,
        CreateView,UpdateView,DeleteView)

class EmployeeListView(ListView):
    model= Employees
    template_name = 'Employee/employees_list.html'
    context_object_name = 'employees_list'



class EmployeeDetailView(DetailView):
    model = Employees
    template_name = 'Employee/employees_detail.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employees
    fields = '__all__'
    template_name = 'Employee/employees_form.html'
    context_object_name = 'form'


class EmployeeUpdateView(UpdateView):
    model = Employees
    fields = '__all__'

class EmployeeDeleteView(DeleteView):
    model = Employees
    success_url = '/employee/'
    template_name = 'Employee/employees_confirm_delete.html'
    context_object_name = 'employees'
