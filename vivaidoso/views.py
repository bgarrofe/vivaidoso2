from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from forms import MyRegistrationForm, UploadFileForm, UserProfileForm, EmpresaForm
from vivaidoso.models import Estado, Cidade, Bairro, Empresa, UploadFile
import json

def index(request):
    return render(request, 'vivaidoso/index.html', {})
    
def sobre_nos(request):
    return render(request, 'vivaidoso/sobre-nos.html', {})

def contatos(request):
    return render(request, 'vivaidoso/contatos.html', {})

@login_required
def pesquisar(request, cod=None):
    if cod:
        try:
            empresa = Empresa.objects.get(id=cod)
        except Empresa.DoesNotExist:
            response_data = {}
            response_data['result'] = 'Empresa does not exist!'
            response_data['status'] = 'error'
            return HttpResponse(json.dumps(response_data),content_type="application/json")
        try:
            images = UploadFile.objects.filter(empresa=empresa)
        except Empresa.DoesNotExist:   
            images = None
        
        return render(request, 'vivaidoso/empresa.html', {'empresa': empresa, 'images': images})
    else:
        empresas = Empresa.objects.all()
        result = []
        response_data = {}
        for empresa in empresas:
            id = empresa.id
            nome = empresa.nome
            bairro = empresa.bairro.desc_bairro
            descricao = empresa.descricao
            try:
                image = UploadFile.objects.filter(empresa=empresa)[:1].get()
                image = image.file.url
            except UploadFile.DoesNotExist:
                image = None
            result.append({'id': id, 'nome': nome, 'bairro': bairro, 'descricao': descricao, 'image': image})

        #empresas = json.dumps(response_data)
        #images = UploadFile.objects.filter(empresa__in=lista)
        return render(request, 'vivaidoso/pesquisar.html', {'empresas': result})

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

def empresa(request, cod=None):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if cod:
                try:
                    empresa = Empresa.objects.get(id=cod)
                except Empresa.DoesNotExist:
                    empresa = None
            else:
                empresa = None

            form = EmpresaForm(request.POST or None,instance=empresa)
            response_data = {}
            if form.is_valid():
                form.save()
                response_data['result'] = 'Model updated!'
                response_data['status'] = 'success'
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            else:
                response_data['result'] = 'Form not valid!'
                response_data['data'] = form.errors
                response_data['status'] = 'error'
                return HttpResponse(json.dumps(response_data),content_type="application/json")
                #return render(request, 'dashboard/empresa_detail.html', {'form': form})
        else:
            if cod:
                try:
                   empresa = Empresa.objects.get(id=cod)
                except Empresa.DoesNotExist:
                   empresa = None
                form = EmpresaForm(instance=empresa)
                
                try:
                    images = UploadFile.objects.filter(empresa=empresa)
                except UploadFile.DoesNotExist:
                    images = None
                        
                #return HttpResponse(form.as_p()) # return a html str
                return render(request, 'dashboard/empresa_detail.html', {'form': form, 'images': images})
            else:
                form = EmpresaForm()
                return render(request, 'dashboard/empresa.html', {'form': form})
    else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path)) 

def profile(request):
    if request.user.is_authenticated():
        if request.method == 'POST': # not being used
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return render(request, 'dashboard/profile.html', {'form': form})
        else:
            profile = UserProfileForm()
            return render(request, 'dashboard/profile.html', {'profile': profile})
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def profile_update(request): # update bio, location, gender and birth date
    if request.user.is_authenticated():
        if request.method == 'POST':
            form = UserProfileForm(request.POST)
            form.save()
            return HttpResponse("Post ok!")
        else:
            return HttpResponse("Post not ok!")
    else:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def ajax_empresas(request):
    
    dados = Empresa.objects.all().values_list('id', 'nome')
    
    data = json.dumps(list(dados))
    
    return HttpResponse(data, content_type='application/json')

@csrf_exempt
def ajax_upload_file(request, cod=None):
    if request.user.is_authenticated():
        if request.method == 'POST':
            if cod:
                try:
                    empresa = Empresa.objects.get(id=cod)
                except Empresa.DoesNotExist:
                    empresa = None
                    response_data['result'] = 'Empresa does not exist!'
                    response_data['status'] = 'error'
                    return HttpResponse(json.dumps(response_data),content_type="application/json")
            else:
                empresa = None
                response_data['result'] = 'Cod not informed!'
                response_data['status'] = 'error'
                return HttpResponse(json.dumps(response_data),content_type="application/json")
            
            form = UploadFileForm(request.POST, request.FILES, instance=empresa)
            response_data = {}
            if form.is_valid():
                new_file = UploadFile(empresa=empresa, file = request.FILES['file'])
                new_file.save()
                form = EmpresaForm()
                return render(request, 'dashboard/empresa.html', {'form': form})
            else:
                response_data['result'] = 'Form not valid!'
                response_data['data'] = form.errors
                response_data['status'] = 'error'
                return HttpResponse(json.dumps(response_data),content_type="application/json")