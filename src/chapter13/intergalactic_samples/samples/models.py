from django.db import models
from django.contrib.auth.models import User

class Sample(models.Model):
    SAMPLE_TYPES = [
        ('ROCK', 'Rock'),
        ('SOIL', 'Soil'),
        ('LIQUID', 'Liquid'),
        ('GAS', 'Gas'),
        ('ICE', 'Ice'),
        ('ORGANIC', 'Organic'),
    ]

    sample_id = models.IntegerField(unique=True, primary_key=True)
    planet = models.CharField(max_length=100)
    sample_type = models.CharField(max_length=20, choices=SAMPLE_TYPES)
    date_collected = models.DateField()
    description = models.TextField()
    mass = models.FloatField(help_text="Mass in grams")
    collector = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.sample_id} - {self.planet} ({self.sample_type})"

    class Meta:
        ordering = ['-date_collected']