from django.db import models
from adaptor.model import CsvModel
from adaptor.fields import DateField, FloatField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=140)  
    birth_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username