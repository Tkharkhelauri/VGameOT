from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Age(models.Model): #ყოველთვის ეს მშობელი კლასი გადაეცემა
    age = models.CharField(max_length=20)

    def __str__(self): # როგორ გამოჩნდეს ადმინში
        return self.age


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Game(models.Model):
    creator = models.ForeignKey('User', on_delete=models.SET("Unknown Creator"))
    name = models.CharField(max_length=200)
    picture = models.ImageField(null=True, blank=True)
    equipment = models.CharField(max_length=200)
    category = models.ManyToManyField(Category, blank=True, related_name='games') #Many To Many
    recommendedAges = models.ForeignKey(Age, on_delete=models.PROTECT) #One To Many
    numberOfPlayers = models.CharField(max_length=200)
    keyFeatures = models.CharField(max_length=2000)
    tips = models.CharField(max_length=500)
    description = models.TextField(max_length=2000)
    howToPlay = models.TextField(max_length=20000)
    content = models.FileField(null=True)

    created = models.DateTimeField(auto_now_add=True)  #შენახვის დრო
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.name


class User(AbstractUser):
    games = models.ManyToManyField(Game, blank=True, related_name='users')

    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default='avatar.png')



