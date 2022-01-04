from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

def create_sample_user(email='test@email.com', password='testpass'):
    """Create a sample user"""
    return get_user_model().objects.create_user(email, password)

class Command(BaseCommand):
    """Django command to create sample user"""

    def handle(self, *args, **options):
        """Create sample user"""
        create_sample_user()
