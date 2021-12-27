from core import views
from django.urls import path

urlpatterns = [
    path('emps/', views.employee_view),
]
