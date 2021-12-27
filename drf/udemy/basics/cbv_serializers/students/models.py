from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


class Student(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(decimal_places=3, max_digits=10)

    def __str__(self):
        return f'{self.id} | {self.name} | {self.score}'


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
