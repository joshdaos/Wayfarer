from django.db import models

# Create your models here.


class UserProfile(models.Model):

    name = models.CharField(max_length=100)
    currentcity = models.CharField(max_length=250)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
