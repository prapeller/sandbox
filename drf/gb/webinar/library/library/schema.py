from django.shortcuts import get_object_or_404

import graphene
import graphene_django

from authors.models import Book, Author, Bio


class BookType(graphene_django.DjangoObjectType):
    class Meta:
        model = Book
        fields = '__all__'


class BookMutation(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String(required=False)

    book = graphene.Field(BookType)

    @classmethod
    def mutate(cls, root, info, id, name=None):
        book = get_object_or_404(Book, pk=id)
        if name:
            book.name = name
            book.save()
        return BookMutation(book=book)


class AuthorType(graphene_django.DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'


class BioType(graphene_django.DjangoObjectType):
    class Meta:
        model = Bio
        fields = '__all__'


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value='stranger'))
    goodbye = graphene.String()

    all_books = graphene.List(BookType)
    book_by_id = graphene.Field(BookType, id=graphene.Int(required=True))
    all_authors = graphene.List(AuthorType)
    author_by_id = graphene.Field(AuthorType, id=graphene.Int(required=True))
    all_bios = graphene.List(BioType)
    bio_by_id = graphene.Field(BioType, id=graphene.Int(required=True))
    bios_by_author_name = graphene.List(BioType, name=graphene.String(required=False))

    def resolve_hello(root, info, name):
        return f'hi {name}!'

    def resolve_goodbye(root, info):
        return 'bye-bye!'

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_book_by_id(root, info, id):
        # return get_object_or_404(Book, pk=id)
        # return Book.objects.get(pk=id)
        try:
            obj = Book.objects.get(pk=id)
        except Book.DoesNotExist:
            return None
        return obj

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_all_bios(root, info):
        return Bio.objects.all()

    def resolve_bios_by_author_name(root, info, name=None):
        all = Bio.objects.all()
        if name:
            return all.filter(author__first_name=name)
        return all


class Mutation(graphene.ObjectType):
    update_book = BookMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
