from django.db import models

from fbv_crud_app.models import Student


class Course(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    rating = models.IntegerField()
    students = models.ManyToManyField(Student, related_name='courses')

    def __str__(self):
        return self.name