from rest_framework.routers import DefaultRouter
from django.urls import path,include
from Employee.api import views

router = DefaultRouter()
router.register('emplopyees',views.EmployeeModelViewset)


urlpatterns= [
    path('',include(router.urls))
]