# membuat form
from django import forms

# from django.contrib.auth.models import User as UserModel
from .models import User as UserModel


class UserForm(forms.ModelForm):
    error_css_class = 'error'

    class Meta:
        model = UserModel
        fields = (
            'first_name' ,
            'last_name', 
            'username',
            'email',
            'password',
            # 'is_superuser',
            # 'is_staff',
            'role'
            # 'is_kprodi',
            # 'is_dosen',
            # 'is_assesor',
        )

        labels = {
            'first_name': 'Nama Depan',
            'last_name' : 'Nama Belakang',
            'password' : 'Password default: "default_password"',
            # 'is_superuser' : 'Super User',
            # 'is_staff' : 'Pakar',
            # 'role' : 'Roles Permission Functionality',
            'is_kprodi': 'Kepala Prodi',
            'is_dosen': 'Dosen',
            'is_assesor': 'Assesor Akreditasi',
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
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'value': 'indonesiapower_expert',
                    'readonly':'readonly',
                }
            ),
            # 'is_superuser': forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #         'required': 'required',
            #     }
            # ),
            # 'is_staff': forms.Select(
            #     attrs={
            #         'class': 'form-control',
            #         'required': 'required',
            #     }
            # ),
            'role': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'required',
                }
            ),
            # 'is_kprodi': forms.CheckboxInput(
            #     attrs={
            #         'class': 'form-control',
            #         # 'required': 'required',
            #     }
            # ),
            # 'is_dosen': forms.CheckboxInput(
            #     attrs={
            #         'class': 'form-control',
            #         # # 'required': 'required',
            #     }
            # ),
            # 'is_assesor': forms.CheckboxInput(
            #     attrs={
            #         'class': 'form-control',
            #         # # 'required': 'required',
            #     }
            # ),
        }
