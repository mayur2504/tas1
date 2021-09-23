from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms

from .models import BlogPost

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password' ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label='Old Password', strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))
    new_password1 = forms.CharField( label='New Password', strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}))
    new_password2 = forms.CharField(label='Confirm Password', strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','autofocus':True,'class':'form-control'}))


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control'}))

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['desc']
        labels = {'desc':'Description'}
        widgets = {'desc':forms.Textarea(attrs={'class':'form-control'})}

class UserForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),
        'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}

class AdminForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'