from django import forms
from app.models import *
from django.core import validators
class UserMF(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email','password']
        help_texts = {'username':''}
        widgets = {
            'username':forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the username',
            }),
            'email':forms.EmailInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the Email'
            }),
            'password':forms.PasswordInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the Password'
            }),
        }

class ProfileMF(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','mobile','address','profile_pic']
        widgets = {
            'address':forms.Textarea(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the Address',
            }),
            'mobile':forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the mobile'
            }),
            'first_name':forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the first_name'
            }),
            'last_name':forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the last-name'
            }),
        }
    

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the username',
            }))
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the Password'
            }))

class ProductMF(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id','product_name','product_description','product_prize']
        widgets = {
            'product_id':forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the product_id',
            }),
            'product_name':forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the product_name'
            }),
            'product_description':forms.Textarea(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the product_description'
            }),
            'product_prize':forms.TextInput(attrs={
                'class' : 'form-control text-center',
                'placeholder' : 'Enter the product_prize',
            }),
        }
        help_texts = {
            'product_prize':'Enter the values in decimals'
        }