from django.core.management import BaseCommand
from django.db import connection

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):

        cur = connection.cursor()
        cur.execute("""
        DELETE FROM users_user;
        """)

        for i in range(10):
            if i == 0:
                user = User.objects.create_superuser('admin', 'admin@test.com', 'pass')
                user.first_name = f'superuser_first_name'
                user.last_name = f'superuser_last_name'
            else:
                user = User.objects.create_user(f'user_{i}', f'user_{i}@test.com', 'pass')
                user.first_name = f'user_{i}_first_name'
                user.last_name = f'user_{i}_last_name'
            user.save()
