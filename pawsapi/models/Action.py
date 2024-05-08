from django.db import models

class Action(models.Model):
    type = models.CharField(max_length=100)
