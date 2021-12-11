"""library URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
# BaseRouter
from authors.views import AuthorViewSet, get_authors_view, post_authors_view, get_bio_view, \
    get_book_view, BioViewSet

# /authors/ - GET, POST
# /authors/1/ - GET 1, PUT, PUT/PATCH/ DELETE

# router = DefaultRouter()
router = SimpleRouter()
router.register('authors', AuthorViewSet)
router.register('bios', BioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    path('api/get_authors/', get_authors_view),
    path('api/get_authors/<int:pk>/', get_authors_view),
    path('api/post_authors/', post_authors_view),
    path('api/post_authors/<int:pk>/', post_authors_view),

    path('api/get_bios/', get_bio_view),
    path('api/get_bios/<int:pk>/', get_bio_view),
    # path('api/post_bios/', post_bio_view),
    # path('api/post_bios/<int:pk>/', post_bio_view),

    path('api/get_books/', get_book_view),
    path('api/get_books/<int:pk>/', get_book_view),
    # path('api/post_books/', post_book_view),
    # path('api/post_books/<int:pk>/', post_book_view),
]
