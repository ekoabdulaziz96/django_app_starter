# membuat form
from django import forms

# from django.contrib.auth.models import User as UserModel
from .models import User as UserModel



class UserAuthForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = UserModel
        fields = (
            'first_name' ,
            'last_name', 
            'username',
            'email',
        )

        labels = {
            'first_name': 'Nama Depan',
            'last_name' : 'Nama Belakang',
        }

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nama depan',
                    'required': 'required',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nama belakang',
                    'required': 'required',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nama_depan_belakang',
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'nama@gmail.com',
                }
            ),
        }
