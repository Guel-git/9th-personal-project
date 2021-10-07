from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '아이디'}), 'password1': forms.PasswordInput(attrs={'class': 'form-control','placeholder': '비밀번호'}), 'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '비밀번호 확인'})}