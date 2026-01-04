from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate

class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    widets = {
        'full_name': forms.TextInput(attrs={'placeholder': 'Enter your full name'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        'password': forms.TextInput(attrs={'placeholder': 'Create a password'}),
        'confirm_password': forms.TextInput(attrs={'placeholder': 'Confirm your password'}),
    }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("Passwords do not match")


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
        max_length=254,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if email and password:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise ValidationError("User with this email does not exist")
            
            user = authenticate(email=user.email, password=password)
            if user is None:
                raise ValidationError("Incorrect password")
        
        return cleaned_data
