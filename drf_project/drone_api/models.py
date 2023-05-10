# models.py

from django.db import models


class Drone(models.Model):
    SERIAL_NUMBER_MAX_LENGTH = 100
    MODEL_CHOICES = [
        ('Lightweight', 'Lightweight'),
        ('Middleweight', 'Middleweight'),
        ('Cruiserweight', 'Cruiserweight'),
        ('Heavyweight', 'Heavyweight'),
    ]
    STATE_CHOICES = [
        ('IDLE', 'Idle'),
        ('LOADING', 'Loading'),
        ('LOADED', 'Loaded'),
        ('DELIVERING', 'Delivering'),
        ('DELIVERED', 'Delivered'),
        ('RETURNING', 'Returning'),
    ]

    serial_number = models.CharField(max_length=SERIAL_NUMBER_MAX_LENGTH)
    model = models.CharField(max_length=20, choices=MODEL_CHOICES)
    weight_limit = models.PositiveIntegerField(default=500)
    battery_capacity = models.PositiveIntegerField(default=100)
    state = models.CharField(max_length=20, choices=STATE_CHOICES)


class Medication(models.Model):
    name = models.CharField(max_length=100)
    weight = models.PositiveIntegerField()
    code = models.CharField(max_length=100)
    image = models.ImageField(upload_to='medication_images/')
