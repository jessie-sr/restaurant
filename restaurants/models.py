from django.db import models

# Definition of the models.
class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=100)
    rating = models.FloatField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name