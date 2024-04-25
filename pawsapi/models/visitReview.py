from django.db import models
from .visit import Visit
from .customer import Customer


class VisitReview(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateField()
