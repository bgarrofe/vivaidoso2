from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers
from forms import MyRegistrationForm, UploadFileForm, UserProfileForm
import json
from dashboard.models import Indice, Dados

def index(request):
	if request.user.is_authenticated():
		return render(request, 'dashboard/index.html', {})
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
	
def register(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)     # create form object
        if form.is_valid():
            form.save()
            return HttpResponse("Form is valid!")
        else:
            return HttpResponse("Form is NOT valid!")
    
    else:
        # show registration form
        form = MyRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})
    
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
        
def analysis_panel(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html', {})
    else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def indexes(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard/indexes.html', {})
    else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def composites(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard/index.html', {})
    else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    
def ajax_indexes(request):
    indices = Indice.objects.all()
    data = serializers.serialize("json", indices)
    return HttpResponse(data, content_type='application/json')

def ajax_price_index(request, cod='VALE001'):
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    
    
    indice = Indice.objects.get(cod=cod)
    dados = Dados.objects.filter(indice=indice)
    data = serializers.serialize("json", dados)
    return HttpResponse(data, content_type='application/json')
