from django.db import models
from django.contrib.auth.models import User
from .visitType import VisitType
from .visitFrequency import VisitFrequency
from .petType import PetType
from .action import Actions

class Visit(models.Model):
    visit_type = models.ForeignKey(VisitType, on_delete=models.CASCADE, related_name="visits")
    visit_start_date = models.DateField()
    visit_end_date = models.DateField()
    date = models.DateTimeField(auto_now_add=True)
    visit_frequency = models.ForeignKey(VisitFrequency, on_delete=models.CASCADE)
    pet_type = models.ForeignKey(PetType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="visits")
    actions = models.ManyToManyField(Actions, through="VisitActions", related_name="visits")
