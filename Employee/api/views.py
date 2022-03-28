from Employee.models import Employees
from Employee.api.serializers import EmployeeSerializer
from rest_framework import viewsets

class EmployeeModelViewset(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer
