from django.db import models
from django.contrib.auth.models import User
from .Visit import Visit


class VisitReview(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date = models.DateField()
