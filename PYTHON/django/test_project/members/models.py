from django.db import models

# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

# this makes the two names appear in the admin panel instead of the default object(1) like stuff
    def __str__(self):
        return f"{self.firstname} {self.lastname}"