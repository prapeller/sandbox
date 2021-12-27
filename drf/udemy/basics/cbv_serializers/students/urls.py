from django.urls import path, include
from .views import StudentModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

"""
from .views import StudentList, StudentDetail

urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:pk>/', StudentDetail.as_view()),
]
"""