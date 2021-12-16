from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorModelViewSet, BookModelViewSet

router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('books', BookModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
