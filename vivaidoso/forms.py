# -*- coding: latin-1 -*-
from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm
from vivaidoso.models import UserProfile, Empresa, Bairro, UploadFile
from tinymce.widgets import TinyMCE
import datetime
from multiselectfield import MultiSelectFormField

GENDER_CHOICES = (
    (1, "Not defined"),
    (2, "Male"),
    (3, "Female")
)

MY_CHOICES = (
    (1, 'Gratuito'),
    (2, 'Até R$ 1.000'),
    (3, 'R$ 1.000 a 3.000'),
    (4, 'R$ 3.000 a 5.000'),
    (5, 'R$ 5.000 a 7.000'),
    (6, 'R$ 7.000 a 10.000')
)

MY_CHOICES2 = (
    (1, 'Individual'),
    (2, 'Duplo'),
    (3, 'Triplo'),
    (4, 'Quádruplo')
)

MY_CHOICES3 = (
    (1, 'Grau 1'),
    (2, 'Grau 2'),
    (3, 'Grau 3')
)

MY_CHOICES4 = (
    (1, 'Masculino'),
    (2, 'Feminino'),
    (3, 'Misto')
)

MY_CHOICES5 = (
    (1, 'Nenhum'),
    (2, 'Cuidador individual 24hrs'),
    (3, 'Fisioterapeuta'),
    (4, 'Terapia Ocupacional'),
    (5, 'Psicólogo'),
    (6, 'Acompanhamento médico')
)

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}))
    first_name = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}))
    last_name = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}))
    username = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password1 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
	
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.is_active = False

        if commit:
            user.save()
            
        return user

class UploadFileForm(forms.ModelForm):
    title = forms.CharField(required = False, max_length=50)
    file = forms.FileField()
    
    class Meta:
        model = UploadFile
        fields = ('title', 'file')
    
class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required = False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Bio'}))
    location = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
    #gender = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    gender = forms.ChoiceField(choices = GENDER_CHOICES, required = False, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    birth_date = forms.DateField(required = False, initial=datetime.date.today, widget=forms.DateInput(attrs={'id': 'data_1', 'class': 'form-control'}))
    
    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'gender', 'birth_date')        

class EmpresaForm(forms.ModelForm):
    nome = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}))
    descricao = forms.CharField(required = True, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descrição', 'rows': '5'}))
    bairro = forms.ModelChoiceField(required = True, empty_label="Selecionar...", queryset=Bairro.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    nat_juridica = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Natureza Jurídica'}))
    horario_visita = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Horário de Visita'}))
    faixa_valor = forms.MultipleChoiceField(required = False, choices=MY_CHOICES, widget=forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Faixa de Valor Mensal'}))
    leitos = forms.MultipleChoiceField(required = False, choices=MY_CHOICES2, widget=forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Leitos'}))
    dependencia = forms.ChoiceField(required = False, choices=MY_CHOICES3, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Grau de Dependência'}))
    sexo = forms.MultipleChoiceField(required = False, choices=MY_CHOICES4, widget=forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Sexo'}))
    servicos_incl = forms.MultipleChoiceField(required = False, choices=MY_CHOICES5, widget=forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Serviços incluídos'}))
    lot_maxima = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Lotação Máxima'}))
    apresentacao = forms.CharField(required = False, widget=TinyMCE())
    servicos = forms.CharField(required = False, widget=TinyMCE())
    admissao = forms.CharField(required = False, widget=TinyMCE())
    atividades = forms.CharField(required = False, widget=TinyMCE())
    localizacao = forms.CharField(required = False, widget=TinyMCE())
    
    class Meta:
        model = Empresa
        fields = ('nome', 'descricao', 'bairro', 'nat_juridica', 'horario_visita', 'lot_maxima', 'apresentacao', 'servicos', 'admissao', 'atividades', 'localizacao', 'faixa_valor', 'leitos', 'dependencia', 'sexo', 'servicos_incl')