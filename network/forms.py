from datetime import date
from attr import attrs
from django import forms
from django.conf import settings

#from network.models import Post
from django.forms.models import inlineformset_factory

class RegisterForm(forms.Form):
    registerImageFile = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'id':'registerImageFile',
            'class':'form-control',
            'type': 'file',
            'onchange':'preview()',
            'required':'false',
        }),
        required=False,
    )

    registerFirstName = forms.CharField(
        widget=forms.TextInput(attrs={
            'id':'registerFirstName',
            'class': 'form-control',
            'placeholder': 'First Name',
            'autofocus':'',
        }),
        max_length=40, 
        required=False,
    )

    registerLastName = forms.CharField(
        widget=forms.TextInput(attrs={
            'id':'registerLastName',
            'class': 'form-control',
            'placeholder': 'Last Name',
            'autofocus':'',
        }),
        max_length=40, 
        required=False,
    )

    registerUsername = forms.CharField(
        widget=forms.TextInput(attrs={
            'id':'registerUsername',
            'class': 'form-control',
            'placeholder': 'Username',
            'autofocus':'',
        }),
        max_length=40, 
    )

    registerEmail = forms.EmailField(
        widget=forms.TextInput(attrs={
            'id':'registerEmail',
            'class': 'form-control',
            'placeholder': 'E-mail',
            'autofocus':'',
        }),
        max_length=100, 
    )

    registerPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id':'registerPassword',
            'class':'form-control',
            'placeholder': 'Password',
            'autofocus':'',
        }),
        max_length=100, 
    )

    registerConfPassword = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'id':'registerConfPassword',
            'class':'form-control',
            'placeholder': 'Confirm Password',
            'autofocus':'',
        }),
        max_length=100, 
    )


class PostForm(forms.Form):
    postContent = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-sm',
            'rows': '3',
            'columns': '100',
        }),
        required=False,
    )
