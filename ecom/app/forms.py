from django import forms    # type: ignore
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm  # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.utils.translation import gettext, gettext_lazy as _  # type: ignore
from django.contrib.auth.forms import UsernameField, PasswordChangeForm     # type: ignore
from django.contrib.auth import password_validation     # type: ignore
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    firstname=forms.CharField(required=True,label='First Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname=forms.CharField(required=True,label='last Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    username=forms.CharField(required=True,label='User Name', widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(required=True,label='Email',widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(required=True,label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(required=True,label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model=User
        fields = ['firstname','lastname','username','email','password1','password2']
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TimeInput(attrs={'class':'form-control','autofocus':True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
    
class Password_Change_Form(PasswordChangeForm):
    old_password=forms.CharField(label=_("Old Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1=forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
    new_password2=forms.CharField(label=_(" Confirm Password"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}))
    
class CustomerProfile(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','location','city','state','zipcode']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'zipcode': forms.NumberInput(attrs={'class':'form-control'}),
        }
        