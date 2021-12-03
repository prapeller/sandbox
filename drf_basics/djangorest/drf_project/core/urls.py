from core import views
from django.urls import path

urlpatterns = [
    path('core/', views.employee_view),
]
