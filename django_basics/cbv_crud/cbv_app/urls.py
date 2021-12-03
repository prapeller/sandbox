from django.urls import path

from cbv_app.views import Create, List, Detail, Delete, Update

app_name = '_'


urlpatterns = [
    path('list/', List.as_view(), name='list'),
    path('detail/<int:pk>/', Detail.as_view(), name='detail'),
    path('create/', Create.as_view(), name='create'),
    path('update/<int:pk>/', Update.as_view(), name='update'),
    path('delete/<int:pk>/', Delete.as_view(), name='delete'),
]
