

from django.urls import path
from Employee import views

urlpatterns = [

    path('',views.EmployeeListView.as_view(),name='employeelist'),
    path('<int:pk>/detail/',views.EmployeeDetailView.as_view(),name='employee_detail'),
    path('create/',views.EmployeeCreateView.as_view(),name='employee_create'),
    path('<int:pk>update/',views.EmployeeUpdateView.as_view(),name='employee_update'),
    path('<int:pk>delete/',views.EmployeeDeleteView.as_view(),name='employee_delete'),



]