from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        unique_together = ('name', 'address')

    def average_rating(self):
        return self.reviews.aggregate(models.Avg('rating'))['rating__avg'] or 0
