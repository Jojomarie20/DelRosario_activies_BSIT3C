from django import forms
from django.core.exceptions import ValidationError
from users.models import Users
from users.utils import hash_password, verify_password

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=255)
    email = forms.EmailField()
    name = forms.CharField(max_length=100)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Users.objects.filter(username=username).exists():
            raise ValidationError("Username already exists")
        return username
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Users.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email
        
    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Hash the password before saving
        return hash_password(password)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=255)
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        
        if username and password:
            user = Users.objects.filter(username=username).first()
            if not user:
                raise ValidationError("User does not exist")
            
            if not verify_password(password, user.password):
                raise ValidationError("Incorrect password")
        
        return cleaned_data
