from django.urls import path, include

from rest_framework.routers import DefaultRouter

from recipes import views

app_name = 'recipes'

router = DefaultRouter()
router.register('tags', views.ListTagViewSet),
router.register('ingredients', views.ListIngredientViewSet),


urlpatterns = [
    path('', include(router.urls)),
]
