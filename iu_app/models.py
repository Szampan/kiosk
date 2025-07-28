from django.db import models

class Kiosk(models.Model):
    MODEL_CHOICES = [
        ('A', 'Model A'),
        ('B', 'Model B'),
    ]
    name = models.CharField(max_length=200)
    model = models.CharField(max_length=1, choices=MODEL_CHOICES)
    description = models.TextField()
    count = models.IntegerField(default=1)


class QrReader(models.Model):
    kiosk = models.ManyToManyField(Kiosk)