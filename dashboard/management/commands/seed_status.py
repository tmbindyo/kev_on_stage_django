from django.core.management.base import BaseCommand
# from django_seed import Seed
from dashboard.models import Status
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the Status model with initial data'

    def handle(self, *args, **options):

        # Add your model-specific seed data here
        status_data = [
            {
                'id': "1",
                'name': 'Active',
                'label': 'primary',
                'description': 'Active record',
                'user_id': 1,
            },
            {
                'id': "2",
                'name': 'Inactive',
                'label': 'warning',
                'description': 'Inactive record',
                'user_id': 1,
            },
            {
                'id': "3",
                'name': 'Deleted',
                'label': 'danger',
                'description': 'Deleted record',
                'user_id': 1,
            },
        ]

        # Seed the database
        for data in status_data:
            Status.objects.create(**data)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded Status model'))
