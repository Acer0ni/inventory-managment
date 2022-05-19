from django.db import models


class Items(models.Models):
    name = models.TextField(max_length=50)
