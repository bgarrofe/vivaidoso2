from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers
from forms import MyRegistrationForm, UploadFileForm, UserProfileForm, EmpresaForm
from vivaidoso.models import Estado, Cidade, Bairro
import json

def index(request):
    return render(request, 'vivaidoso/index.html', {})
    
def sobre_nos(request):
    return render(request, 'vivaidoso/sobre-nos.html', {})

def contatos(request):
    return render(request, 'vivaidoso/contatos.html', {})

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

def dashboard(request):
	if request.user.is_authenticated():
		return render(request, 'dashboard/index.html', {})
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def empresa(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = EmpresaForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, 'dashboard/empresa.html', {'form': form})
        else:
            form = EmpresaForm()
            return render(request, 'dashboard/empresa.html', {'form': form})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def profile(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return render(request, 'dashboard/profile.html', {'form': form})
        else:
            form = UploadFileForm()
            profile = UserProfileForm()
            return render(request, 'dashboard/profile.html', {'form': form, 'profile': profile})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def profile_update(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            form.save()
        else:
            return HttpResponse("Post not ok!")
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))