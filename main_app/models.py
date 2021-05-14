from django.db import models
from datetime import date
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):

    name = models.CharField(max_length=100)
    currentcity = models.CharField(max_length=500)
    join_date = models.DateField(default=date.today())
    image = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
