from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('male','Male'),
    ('female', 'Female'),
    ('others', 'Others'),
)

class Moive(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class User(models.Model):
    name = models.CharField(max_length=255)
    age=models.IntegerField()
    gender=models.CharField(max_length=6, choices=GENDER_CHOICES,null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
