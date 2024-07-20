from django.db import models

# Create your models here.
class PlayerStates(models.Model):
    state = models.CharField(max_length=50)
    test = models.DecimalField(max_digits=10, decimal_places=2)