import io

from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.parsers import JSONParser
from .models import Author, Bio, Book
from .serializers import AuthorModelSerializer, AuthorSerializer, BioSerializer, BookSerializer, \
    BioModelSerializer


# client - router/url - view --[     ]--- serializer ---[      ]--- model
#                           request.data                instance


class AuthorViewSet(ModelViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BioViewSet(ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioModelSerializer


def get_bio_view(request, pk=None):
    if pk:
        bio = Bio.objects.get(pk=pk)
        serializer = BioSerializer(bio)
    else:
        bios = Bio.objects.all()
        serializer = BioSerializer(bios, many=True)
    r = JSONRenderer()
    json_data = r.render(serializer.data)
    print(serializer.data)
    return HttpResponse(json_data)

def get_book_view(request, pk=None):
    if pk:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
    else:
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
    r = JSONRenderer()
    json_data = r.render(serializer.data)
    print(serializer.data)
    return HttpResponse(json_data)


def get_authors_view(request, pk=None):
    if pk:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
    else:
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
    r = JSONRenderer()
    json_data = r.render(serializer.data)
    print(serializer.data)
    return HttpResponse(json_data)


@csrf_exempt
def post_authors_view(request, pk=None):
    print(request.body)
    data = JSONParser().parse(io.BytesIO(request.body))

    if request.method == 'POST':
        serializer = AuthorSerializer(data=data)
    elif request.method == 'PUT':
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(instance=author, data=data)
    elif request.method == 'PATCH':
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(instance=author, data=data, partial=True)

    if serializer.is_valid():
        print(serializer.validated_data)
        author = serializer.save()
        serializer = AuthorSerializer(author)
        r = JSONRenderer()
        json_data = r.render(serializer.data)
        print(serializer.data)
        return HttpResponse(json_data)
    else:
        return HttpResponseServerError(
            f'cant validate data: {serializer.errors.get("non_field_errors")}'
            f'{serializer.errors.get("birth_year")}')


