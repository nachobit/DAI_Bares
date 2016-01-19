from django import forms
from django.contrib.auth.models import User
from rango.models import Bares, Tapas

class LoginForm(forms.ModelForm):
	username = forms.SlugField (max_length=8, label='Usuario: ')
	password = forms.SlugField (max_length=8, 
		widget=forms.PasswordInput(),
		label='Password:',
		help_text='Hasta 8 letras')
	class Meta:
		model  = User
		fields = ('username',  'password')


class RegisterForm(forms.ModelForm):
	username = forms.SlugField (max_length=8, label='Usuario:')
	email    = forms.EmailField (label='Email:')
	password = forms.SlugField (max_length=8, 
		help_text="(numeros y letras hasta 8)", 
		widget=forms.PasswordInput(), 
		label='Password:')
	class Meta:
		model  = User
		fields = ('username', 'email', 'password')


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Por favor, introduce la nueva tapa :")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Tapas
        #exclude = ('bar')
        fields = ('barname','name')
