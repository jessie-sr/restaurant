from django.core.management.base import BaseCommand
from restaurants.models import Restaurant  # adjust "your_app" and "Restaurant" to fit your project
import json

class Command(BaseCommand):
    help = 'Populates the database with restaurant data'

    def handle(self, *args, **options):
        data = [
            {"id": 1, "name": "Pasta Paradise", "location": "Rome", "cuisine": "Italian", "rating": 4.5, "contact": {"phone": "123-456-7890", "email": "info@pastaparadise.com"}},
            {"id": 2, "name": "Curry King", "location": "Mumbai", "cuisine": "Indian", "rating": 4.7, "contact": {"phone": "098-765-4321", "email": "contact@currykingdom.com"}},
            {"id": 3, "name": "Sushi Suite", "location": "Tokyo", "cuisine": "Japanese", "rating": 4.9, "contact": {"phone": "234-567-8901", "email": "reservations@sushisuite.com"}},
            {"id": 4, "name": "Taco T", "location": "Mexico City", "cuisine": "Mexican", "rating": 4.4, "contact": {"phone": "345-678-9012", "email": "info@tacoterritory.mx"}}
        ]

        for entry in data:
            restaurant, created = Restaurant.objects.get_or_create(
                id=entry['id'],
                defaults={
                    'name': entry['name'],
                    'location': entry['location'],
                    'cuisine': entry['cuisine'],
                    'rating': entry['rating'],
                    'phone': entry['contact']['phone'],
                    'email': entry['contact']['email']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added {entry["name"]}'))
            else:
                self.stdout.write(f'{entry["name"]} already exists')
