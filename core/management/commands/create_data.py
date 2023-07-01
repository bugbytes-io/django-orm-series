import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from core.models import Restaurant, Rating, Sale


class Command(BaseCommand):
    help = 'Creates application data'

    def handle(self, *args, **kwargs):
        # get or create an admin user
        user = User.objects.filter(username='admin')
        if not user.exists():
            user = User.objects.create_superuser(username='admin', password='test')
        else:
            user = user.first()

        restaurants = [
            {'name': 'Pizzeria 1', 'date_opened': timezone.now() - timezone.timedelta(days=20), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitude': 55.869829854, 'longitude': -4.28583219},
            {'name': 'Pizzeria 2', 'date_opened': timezone.now() - timezone.timedelta(days=27), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitude': 55.862, 'longitude': -4.247},
            {'name': 'Golden Dragon', 'date_opened': timezone.now() - timezone.timedelta(days=15), 'restaurant_type': Restaurant.TypeChoices.CHINESE, 'latitude': 55.953251, 'longitude':  -3.188267},
            {'name': 'Bombay Bustle', 'date_opened': timezone.now() - timezone.timedelta(days=44), 'restaurant_type': Restaurant.TypeChoices.INDIAN, 'latitude': 51.509865, 'longitude':  -0.118092},
            {'name': 'McDonalds', 'date_opened': timezone.now() - timezone.timedelta(days=51), 'restaurant_type': Restaurant.TypeChoices.FASTFOOD, 'latitude': 53.483959, 'longitude':  -2.244644},
            {'name': 'Taco Bell', 'date_opened': timezone.now() - timezone.timedelta(days=12), 'restaurant_type': Restaurant.TypeChoices.FASTFOOD, 'latitude': 53.413959, 'longitude':  -2.254644},
            {'name': 'Chinese 2', 'date_opened': timezone.now() - timezone.timedelta(days=31), 'restaurant_type': Restaurant.TypeChoices.CHINESE, 'latitude': 53.400002, 'longitude':  -2.983333},
            {'name': 'Chinese 3', 'date_opened': timezone.now() - timezone.timedelta(days=71), 'restaurant_type': Restaurant.TypeChoices.CHINESE, 'latitude': 55.070859, 'longitude':  -3.60512},
            {'name': 'Indian 2', 'date_opened': timezone.now() - timezone.timedelta(days=46), 'restaurant_type': Restaurant.TypeChoices.INDIAN, 'latitude': 53.350140, 'longitude':  -6.266155},
            {'name': 'Mexican 1', 'date_opened': timezone.now() - timezone.timedelta(days=52), 'restaurant_type': Restaurant.TypeChoices.MEXICAN, 'latitude': 51.481583, 'longitude':  -3.179090},
            {'name': 'Mexican 2', 'date_opened': timezone.now() - timezone.timedelta(days=50), 'restaurant_type': Restaurant.TypeChoices.MEXICAN, 'latitude': 55.847258, 'longitude':  -4.440114},
            {'name': 'Pizzeria 3', 'date_opened': timezone.now() - timezone.timedelta(days=4), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitude': 54.966667, 'longitude':  -1.600000},
            {'name': 'Pizzeria 4', 'date_opened': timezone.now() - timezone.timedelta(days=61), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitude': 48.856614, 'longitude':  2.3522219},
            {'name': 'Italian 1', 'date_opened': timezone.now() - timezone.timedelta(days=37), 'restaurant_type': Restaurant.TypeChoices.ITALIAN, 'latitude': 41.902782, 'longitude':  12.496366},
        ]

        Restaurant.objects.all().delete()
        for r in restaurants:
            Restaurant.objects.create(**r)

        restaurants = Restaurant.objects.all()

        # create some ratings
        for _ in range(30):
            Rating.objects.create(
                restaurant=random.choice(restaurants),
                user=user,
                rating=random.randint(1,5)
            )

        # create some sales
        for _ in range(100):
            Sale.objects.create(
                restaurant=random.choice(restaurants),
                income=random.uniform(5, 100),
                datetime=timezone.now() - timezone.timedelta(days=random.randint(1,50))
            )