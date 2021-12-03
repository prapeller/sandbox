from django.db import models
from django.contrib.postgres.fields import ArrayField


class TravelPoints(models.Model):
    city = models.CharField(unique=True, null=False, blank=False, max_length=10)

    def __str__(self):
        return self.city


class Passenger(models.Model):
    id = models.SmallAutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    travel_points = models.ManyToManyField(TravelPoints, max_length=2)

    # travel_points = ArrayField(models.CharField(max_length=10, choices=(
    # ('1', 'point_1'), ('2', 'point_2'), ('3', 'point_3'))),
    # default=list(('1', '2')))

    def __str__(self):
        return f'{self.id} | {self.first_name} | {self.last_name} | ' \
               f'{self.travel_points.city}'
