from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from recipes import serializers
from recipes.models import Tag, Ingredient, Recipe


class BaseUserOwnedRecipeAttrsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                                      viewsets.GenericViewSet):
    """Base viewset for user owned recipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """Create a new user based attribute"""
        serializer.save(user=self.request.user)


class ListTagViewSet(BaseUserOwnedRecipeAttrsViewSet):
    """List tags in the db"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class ListIngredientViewSet(BaseUserOwnedRecipeAttrsViewSet):
    """List ingredients in the db"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class ListRecipeViewSet(viewsets.ModelViewSet):
    """List recipes in the db"""
    queryset = Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user"""
        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return appropriate serializer class for corresponding action"""
        if self.action == 'retrieve':
            return serializers.RecipeDetailSerializer

        return self.serializer_class