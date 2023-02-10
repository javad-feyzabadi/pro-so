from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email = email).exists()
        if user:
            raise ValidationError("This Email Already Exists!")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user = User.objects.filter(username = username).exists()
        if user :
            raise ValidationError("This UserName Already Exists!")
        return username
    
    # For when you have to compare two fields and def Clean must be override
    def clean(self):
        cd = super().clean()
        p1 = cd.get('password1')
        p2 = cd.get('password2')
        if p1 and p2 and p1 != p2 :
            raise ValidationError('Thiss Passwords Not Match')
