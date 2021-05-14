from django.db import models
from datetime import date

# Create your models here.


class UserProfile(models.Model):

    name = models.CharField(max_length=100)
    currentcity = models.CharField(max_length=500)
    join_date = models.DateField(default=date.today())
    img = models.CharField(max_length=500)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
