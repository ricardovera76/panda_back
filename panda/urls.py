from django.urls import path
from .views import Drivers, Employees, PandaApi, Routes, SingleData, TrainingEmployees, Vans

urlpatterns = [
    path('', PandaApi.as_view()),
    path('driver/', Drivers.as_view()),
    path('employee/', Employees.as_view()),
    path('route/', Routes.as_view()),
    path('van/', Vans.as_view()),
    path('training-employee/', TrainingEmployees.as_view()),
    path('single/', SingleData.as_view())
]