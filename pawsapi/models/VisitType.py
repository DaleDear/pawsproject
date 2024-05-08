from django.db import models


class VisitType(models.Model):
   visit_type = models.CharField(max_length=100)
   
