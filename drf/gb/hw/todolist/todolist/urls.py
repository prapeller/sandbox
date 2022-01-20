"""todolist URL Configuration

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
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

from graphene_django.views import GraphQLView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from todo.views import ProjectModelViewSet, TodoModelViewSet
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoModelViewSet)

schema_view = get_schema_view(
    openapi.Info(title='Todo List',
                 default_version='v1',
                 description='Todo list used by Users in their Projects',
                 contact=openapi.Contact(email='test@test.com'),
                 license=openapi.License(name='MIT')
                 ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path(r'admin/', admin.site.urls),
    re_path(r'^api/(?P<version>.\d)/', include(router.urls)),
    path(r'api-auth/', include('rest_framework.urls')),
    path(r'api-token-auth/', obtain_auth_token),

    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),

    path(r'graphql/', GraphQLView.as_view(graphiql=True)),

    path('', TemplateView.as_view(template_name='index.html')),
]
