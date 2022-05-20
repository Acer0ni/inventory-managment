from pyexpat import model
from django.db import models


class Item(models.Model):
    name = models.TextField(max_length=100)
    amount = models.IntegerField()
