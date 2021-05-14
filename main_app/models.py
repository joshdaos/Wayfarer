from django.db import models
from django.db.models import Model, DateTimeField
import time
# Create your models here.

class UserProfile(Model):
    name = models.CharField(max_length=100)
    currentcity = models.CharField(max_length=500)
    join_date = models.DateTimeField(auto_now_add=True)
    img = models.CharField(max_length=500)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
