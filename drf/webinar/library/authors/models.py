from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_year = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Bio(models.Model):
    text = models.CharField(max_length=64)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} | {self.text}'


class Book(models.Model):
    name = models.CharField(max_length=64, default='name')
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f'{self.name} | {self.authors}'
