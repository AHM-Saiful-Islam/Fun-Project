from django.db import models

# Create your models here.
class Task(models.Model):
    DAYS_OF_WEEK = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    time = models.TimeField()

    def __str__(self):
        return f"{self.title} - {self.day}"
