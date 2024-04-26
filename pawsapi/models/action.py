from django.db import models

class Actions(models.Model):
    type = models.CharField(max_length=100)
