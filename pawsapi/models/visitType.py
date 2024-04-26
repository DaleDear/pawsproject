from django.db import models


class VisitType(models.Model):
   type = models.CharField(max_length=100)
   
