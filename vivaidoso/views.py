from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers
from forms import MyRegistrationForm, UploadFileForm, UserProfileForm
from vivaidoso.models import Estado, Cidade, Bairro
import json

def index(request):
	if request.user.is_authenticated():
		return render(request, 'vivaidoso/index.html', {})
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
def sobre_nos(request):
	if request.user.is_authenticated():
		return render(request, 'vivaidoso/sobre-nos.html', {})
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def contatos(request):
	if request.user.is_authenticated():
		return render(request, 'vivaidoso/contatos.html', {})
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def ajax_estados(request):
    estados = Estado.objects.all()
    data = serializers.serialize("json", estados)
    return HttpResponse(data, content_type='application/json')

def ajax_cidades(request, estado):
    cidades = Cidade.objects.filter(estado=estado)
    data = serializers.serialize("json", cidades)
    return HttpResponse(data, content_type='application/json')

def ajax_bairros(request, cidade):
    bairros = Bairro.objects.filter(cidade=cidade)
    data = serializers.serialize("json", bairros)
    return HttpResponse(data, content_type='application/json')