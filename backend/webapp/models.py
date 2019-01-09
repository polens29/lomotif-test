import random

from django.db import models

# Create your models here.

class CardSet(models.Model):
    name = models.CharField(max_length=100, null=False)


class Card(models.Model):
    cardId = models.CharField(max_length=50, null=False)
    name = models.CharField(max_length=255, null=False)
    dbfId = models.IntegerField(null=False)
    text = models.CharField(max_length=255, null=True)
    locale = models.CharField(max_length=10, null=True)
    type = models.CharField(max_length=50, null=False)
    playerClass = models.CharField(max_length=50, null=True)
    cardSet_id = models.IntegerField(null=False)
    health = models.IntegerField(null=True)





