from django.db import models

# Create your models here.

class Player(models.Model):
    username = models.CharField(max_length=30)
    health = models.IntegerField()
    energy = models.IntegerField()

    def __str__(self):
        return self.username

class Card(models.Model):
    name = models.CharField(max_length=30, default='name')
    health = models.IntegerField()
    attack = models.IntegerField()

    def __str__(self):
        return self.name