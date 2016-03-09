from django import forms
from .models import User, MedicalProfile

class UserLoginForm(forms.Form):

	username = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={
							'type' : 'text',
							'placeholder' : 'Ingresa un nombre de usuario'
						}))
	password = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={
							'type' : 'password',
							'placeholder' : 'Ingresa una password'
						}))

	def clean(self):
		user_exist = User.objects.filter(username = self.cleaned_data['username'])
		if not user_exist:
			self.add_error('username', 'El nombre de usuario no existe!')
		else:
			user = User.objects.get(username = self.cleaned_data['username'])
			if not user.check_password(self.cleaned_data['password']):
				self.add_error('password', 'El password es incorrecto')


class UserCreateForm(forms.ModelForm):

	class Meta:
		model= User
	
		fields=('username', 'first_name', 'last_name', 'email', 'password')
		widgets={
			'username':forms.TextInput(attrs={
				'type': 'text',
				'placeholder': 'Ingresa un nombre de usuario'
				}),
			'first_name':forms.TextInput(attrs={
				'type': 'text',
				'placeholder': 'Ingresa tu nombre'
				}),
			'last_name':forms.TextInput(attrs={
				'type': 'text',
				'placeholder': 'Ingresa tu apellido'
				}),
			'password':forms.TextInput(attrs={
				'type': 'password',
				'placeholder': 'Ingresa un password'
				}),
			'email':forms.TextInput(attrs={
				'type': 'email',
				'placeholder': 'Ingresa un a direccion de correo'
				}),
			'num_coleg':forms.TextInput(attrs={
				'type': 'text',
				'placeholder': 'Ingresa el numero del colegiado'
				}),
		}


 