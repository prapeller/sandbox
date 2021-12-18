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
from rest_framework.routers import DefaultRouter, SimpleRouter, BaseRouter
from authors.views import authors_list_view, authors_detail_view, bios_view, books_view
from authors.views import authors_list_api_view, authors_detail_api_view
from authors.views import AuthorListGenericViewSet, AuthorDetailGenericViewSet
from authors.views import GenApiAuthorList, GenApiAuthorDetail
from authors.views import AuthorViewSet
from authors.views import AuthorModelViewSet, BioModelViewSet, BookModelViewSet
from authors.views import AuthorList, AuthorDetail
from authors.views import ActionedAuthorModelViewSet
from authors.views import KwargsParamsAuthorModelViewSet
from authors.views import QueryParamsAuthorModelViewSet
from authors.views import FilteredAuthorModelViewSet
from authors.views import PaginatedAuthorModelViewSet


router = DefaultRouter()
# router = SimpleRouter()
router.register('modelviewset_authors', AuthorModelViewSet)
router.register('modelviewset_bios', BioModelViewSet)
router.register('modelviewset_books', BookModelViewSet)

# router.register('genviewset_list_authors', AuthorListGenericViewSet)
# router.register('genviewset_detail_authors', AuthorDetailGenericViewSet)
# router.register('actioned_authors', ActionedAuthorModelViewSet)
# router.register('params_authors', QueryParamsAuthorModelViewSet)
# router.register('filtered_authors', FilteredAuthorModelViewSet)
# router.register('paginated_authors', PaginatedAuthorModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('fbv/authors/', authors_list_view),
    path('fbv/authors/<int:pk>/', authors_detail_view),

    path('fbv/apiview_authors/', authors_list_api_view),
    path('fbv/apiview_authors/<int:pk>/', authors_detail_api_view),

    path('cbv/authors/', AuthorList.as_view()),
    path('cbv/authors/<int:pk>/', AuthorDetail.as_view()),

    path('cbv/genapi_authors/', GenApiAuthorList.as_view()),
    path('cbv/genapi_authors/<int:pk>/', GenApiAuthorDetail.as_view()),

    path('cbv/viewset_authors/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cbv/viewset_authors/<int:pk>/', AuthorViewSet.as_view({'get': 'retrieve',
                                                                 'put': 'update',
                                                                 'patch': 'partial_update',
                                                                 'delete': 'destroy'})),

    path('cbv/genviewset_authors/', AuthorListGenericViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('cbv/genviewset_authors/<int:pk>/', AuthorDetailGenericViewSet.as_view({'get': 'retrieve',
                                                                 'put': 'update',
                                                                 'patch': 'partial_update',
                                                                 'delete': 'destroy'})),

    path('params_authors/<str:name>/', KwargsParamsAuthorModelViewSet.as_view({'get': 'list'})),
    path('api/', include(router.urls)),

]
