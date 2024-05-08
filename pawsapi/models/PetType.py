from django.db import models

class PetType(models.Model):
    pet_type = models.CharField(max_length=100)
