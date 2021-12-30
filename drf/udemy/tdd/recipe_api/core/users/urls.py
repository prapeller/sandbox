from django.urls import path, include

from rest_framework.routers import DefaultRouter

from users import views

router = DefaultRouter()
# router.register('create', views.CreateUserViewSet, basename='create-user'),

app_name = 'users'

urlpatterns = [
    path('', views.ListCreateUserView.as_view(), name='list-create'),
    path('<int:pk>', views.RetrieveUpdateDestroyUserView.as_view(), name='retrieve-update-destroy')
]
