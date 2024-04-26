from django.db import models
from .visit import Visit
from .action import Actions  # Import the Actions model


class VisitActions(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    action = models.ForeignKey(Actions, on_delete=models.CASCADE)  # Add a foreign key to the Actions model
