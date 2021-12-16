from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import ModelViewSet



class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
