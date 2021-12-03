"""clinicals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from clinicals_app.views import PatientCreateView, PatientListView, PatientUpdateView, \
    PatientDeleteView, analyze, add_data

app_name = 'patients'

urlpatterns = [
    path('create/', PatientCreateView.as_view(), name='create'),
    path('list/', PatientListView.as_view(), name='list'),
    path('update/<int:pk>', PatientUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', PatientDeleteView.as_view(), name='delete'),
    path('analyze/<int:pk>', analyze, name='analyze'),
    path('add_data/<int:pk>', add_data, name='add_data'),
]
