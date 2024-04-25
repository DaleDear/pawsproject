from django.db import models
from .visitType import VisitType
from .customer import Customer


class Visit(models.Model):
    visitType = models.ForeignKey(VisitType, on_delete=models.CASCADE)
    visit_start_date = models.DateField()
    visit_end_date = models.DateField()
    date = models.DateTimeField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
