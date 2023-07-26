from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Recruiter(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
        related_name="recruit"
    )
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    payment_for_found = models.IntegerField(null=True, blank=True)
    bonus_percent = models.DecimalField(max_digits=5, decimal_places=1, null=True, blank=True)



