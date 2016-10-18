from django.db import models
from adaptor.model import CsvModel
from adaptor.fields import DateField, FloatField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField
from .utils import upload_path_handler

# Create your models here.

class UserProfile(models.Model):  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=140)  
    gender = models.CharField(max_length=140)  
    birth_date = models.DateField(null=True, blank=True)

    def __unicode__(self):
        return u'Profile of user: %s' % self.user.username
    
class Estado(models.Model):  
    flg_estado = models.TextField(max_length=2, blank=False)
    desc_estado = models.TextField(max_length=72, blank=False)
    cep1 = models.TextField(max_length=5, blank=False)
    cep2 = models.TextField(max_length=5, blank=False)
    
    def __unicode__(self):
        return u'Estado: %s' % self.desc_estado

class Cidade(models.Model):  
    desc_cidade = models.TextField(max_length=60, blank=False)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return u'Cidade: %s' % self.desc_cidade

class Bairro(models.Model):
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    desc_bairro = models.TextField(max_length=60, blank=False)
    
    def __unicode__(self):
        return u'Bairro: %s' % self.desc_bairro

class Empresa(models.Model):
    nome = models.CharField(max_length=140)
    descricao = models.CharField(max_length=200)
    bairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    nat_juridica = models.CharField(max_length=60)
    horario_visita = models.CharField(max_length=60)
    lot_maxima = models.CharField(max_length=60)
    apresentacao = HTMLField()
    servicos = HTMLField()
    admissao = HTMLField()
    atividades = HTMLField()
    localizacao = HTMLField()
    
    def __unicode__(self):
        return u'Empresa: %s' % self.nome

class UploadFile(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    file = models.FileField(upload_to=upload_path_handler)
    
    def __unicode__(self):
        return u'File: %s' % self.title