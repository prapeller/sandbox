from django.core.management.base import BaseCommand
from django.db import connections

from users.models import User


class Command(BaseCommand):
    """Django command to fill empty db with users"""

    def handle(self, *args, **options):
        users = User.objects.all()
        users.delete()

