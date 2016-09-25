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
        
class Dados(models.Model):
    date = models.DateField()
    value = models.FloatField()
    indice = models.ForeignKey('Indice', on_delete=models.CASCADE)

class Indice(models.Model):
    cod = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    source = models.CharField(max_length=30)
    unit = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Composite(models.Model):
    cod = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    suffix = models.CharField(max_length=2)
    scenario = models.CharField(max_length=30)
    members = models.ManyToManyField(Indice, through='Membership')
    
    def __str__(self):
        return self.name
    
class Membership(models.Model):
    indice = models.ForeignKey(Indice, on_delete=models.CASCADE)
    composite = models.ForeignKey(Composite, on_delete=models.CASCADE)
    weight = models.FloatField()
	
class MyCsvModel(CsvModel):
	date = DateField()
	value = FloatField()

	class Meta:
		delimiter = ";"