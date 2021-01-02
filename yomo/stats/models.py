from django.db import models

class Stats(models.Model):
    name = models.CharField(max_length=32)
    score = models.FloatField()
    color = models.CharField(max_length=7, default='white')

    def __str__(self):
        return self.name
