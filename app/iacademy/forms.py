from django import forms
from .models import Certificate
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class DateInput(forms.DateInput):
    input_type = 'date'
    attrs = {
        'class': "form-control"
    }


class CertificateCreateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'surname', 'date_of_birth', 'grade', 'subject']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control"
                }),
            'surname': forms.TextInput(attrs={
                'class': "form-control"
                }),
            'date_of_birth': DateInput(),
            'grade': forms.NumberInput(attrs={
                'class': "form-control"
                }),
            'subject': forms.TextInput(attrs={
                'class': "form-control"
                }),
        }
