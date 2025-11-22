from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        # Create a default user if none exists
        user, created = User.objects.get_or_create(username='host_user')
        if created:
            user.set_password('password')
            user.save()

        # Create sample listings
        for i in range(1, 11):  # 10 listings
            Listing.objects.create(
                title=f'Sample Listing {i}',
                description=f'Description for listing {i}',
                price_per_night=random.randint(50, 500),
                host=user
            )
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
