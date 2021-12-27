from django.db import models


class Student(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(decimal_places=3, max_digits=10)

    def __str__(self):
        return f'{self.id} | {self.name} | {self.score}'
