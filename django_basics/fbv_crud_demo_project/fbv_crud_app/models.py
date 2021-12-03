from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    test_score = models.FloatField()
    headman = models.ForeignKey('Student', on_delete=models.SET_NULL, related_name='students',
                                default=None, null=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'


class StudentCard(models.Model):

    RED = 'red'
    BLUE = 'blue'

    COLORS = (('r', RED), ('b', BLUE))

    id = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=1, choices=COLORS)
    valid_from = models.DateField()
    valid_to = models.DateField()
    student = models.OneToOneField('Student', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} : {self.color}'
