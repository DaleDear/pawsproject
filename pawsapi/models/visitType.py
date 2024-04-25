from django.db import models
from .petType import PetType

class VisitType(models.Model):
    type = models.CharField(max_length=100)
    petType = models.ForeignKey(PetType, on_delete=models.CASCADE)
