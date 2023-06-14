from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):

        return self.name


class Platform(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Game(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    platform = models.ForeignKey(Platform, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    price = models.FloatField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Key(models.Model):

    value = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value} -- {self.game}'
