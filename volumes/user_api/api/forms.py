from django import forms
from .backends import UserModel

class CustomLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CustomSignupForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['username', 'password', 'email']
        widgets = {
            'password': forms.PasswordInput(),
        }