from django.db import models

from django.db import models

class Accommodation(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField()
    stars = models.FloatField()
    price = models.FloatField()
    image = models.ImageField(upload_to='accommodation_images/')

class Activity(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.CharField(max_length=50)
    price = models.FloatField()
    stars = models.FloatField()
    labels = models.JSONField()
    image = models.ImageField(upload_to='activity_images/')

class Car(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images/')
    price = models.FloatField()
    description = models.JSONField()
    rating = models.FloatField()
    fuelType = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    passengers = models.IntegerField()

class Promo(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='promo_images/')

class Profile(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    travelPreferences = models.JSONField()
    notifications = models.JSONField()
    filters = models.JSONField()
