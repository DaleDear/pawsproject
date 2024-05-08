from django.db import models
from .Visit import Visit
from .Action import Action  # Import the Actions model


class VisitAction(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)  # Add a foreign key to the Actions model
