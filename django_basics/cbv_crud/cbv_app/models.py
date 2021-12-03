from django.db import models
from django.urls import reverse


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    test_score = models.FloatField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('students:detail', kwargs={'pk': self.pk})
