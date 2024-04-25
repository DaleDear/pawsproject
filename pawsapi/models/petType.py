from django.db import models


class PetType(models.Model):
    type = models.CharField(max_length=100)
