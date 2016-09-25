from django import forms            
from django.contrib.auth.models import User   # fill in custom user info then save it 
from django.contrib.auth.forms import UserCreationForm
from dashboard.models import UserProfile
import datetime

GENDER_CHOICES = (
    (1, "Not defined"),
    (2, "Male"),
    (3, "Female")
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

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
    
class UserProfileForm(forms.ModelForm):
    bio = forms.CharField(required = False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Bio'}))
    location = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Location'}))
    #gender = forms.CharField(required = False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    gender = forms.ChoiceField(choices = GENDER_CHOICES, required = False, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    birth_date = forms.DateField(required = False, initial=datetime.date.today, widget=forms.DateInput(attrs={'id': 'data_1', 'class': 'form-control'}))
    
    class Meta:
        model = UserProfile
        fields = ('bio', 'location', 'gender', 'birth_date')
    