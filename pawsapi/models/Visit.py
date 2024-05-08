from django.db import models
from django.contrib.auth.models import User
from .VisitType import VisitType
from .VisitFrequency import VisitFrequency
from .PetType import PetType
from .Action import Action

class Visit(models.Model):
    visit_type = models.ForeignKey(VisitType, on_delete=models.CASCADE, related_name="visits")
    visit_start_date = models.DateField()
    visit_end_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    visit_frequency = models.ForeignKey(VisitFrequency, on_delete=models.CASCADE)
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits")
    actions = models.ManyToManyField(Action, through="VisitAction", related_name="visits")
