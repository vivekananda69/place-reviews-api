# scripts/populate_data.py
import random
from django.contrib.auth import get_user_model
from places.models import Place
from reviews.models import Review

User = get_user_model()

def run():
    users = [
        User.objects.create_user(
            phone=f"9999{i}",
            name=f"User{i}",
            password="test"
        )
        for i in range(5)
    ]

    places = [
        Place.objects.create(
            name=f"Shop{i}",
            address=f"Street{i}"
        )
        for i in range(5)
    ]

    for u in users:
        for p in random.sample(places, 3):
            Review.objects.create(
                user=u,
                place=p,
                rating=random.randint(1, 5)
            )
