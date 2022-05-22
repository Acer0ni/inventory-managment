from django.db import models


class Warehouse(models.Model):
    location = models.TextField(max_length=100)
