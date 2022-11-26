from datetime import date

from attr import attrs
from django import forms
from django.conf import settings

class RegisterForm(forms.Form):
    registerImageFile = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'id':'registerImageFile',
            'class':'form-control',
            'type': 'file',
            'required':'false',
            'hidden': 'true',
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
    postUserImage = forms.TextInput(

    )
    
    postContent = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control form-control-sm post-text-area',
            'id':'postContent',
            'rows': '3',
            'cols': '100',
            'margin-left': '20px',
            'placeholder': 'What''s happening?',
        }),
        required=False,
    )
