from django.db import models
from .visit import Visit
from .petType import PetType


class VisitActions(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    petType = models.ForeignKey(PetType, on_delete=models.CASCADE)
    actions = models.CharField(max_length=255)
