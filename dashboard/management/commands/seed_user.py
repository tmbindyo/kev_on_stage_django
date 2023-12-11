import uuid
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the User model with initial data'

    def handle(self, *args, **options):
        # Add your model-specific seed data here
        user_data = [
            {
                'id': 1,
                'first_name': 'Admin',
                'last_name': '',
                'is_superuser': True,
                'email': 'admin@kevonstage.com',
                'password': make_password('jN56Fi3@G96avgYa'),
            },
        ]

        # Seed the database
        for data in user_data:
            User.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded User model'))
