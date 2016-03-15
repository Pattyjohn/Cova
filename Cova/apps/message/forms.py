from django import forms


class EmailForm(forms.Form):

	subject =forms.CharField(max_length=100,widget=forms.TextInput(attrs={
							'type' : 'text',
							'placeholder' : 'Escribe aqui el asunto'
						}))
	message= forms.CharField(widget=forms.Textarea(attrs={
							'type' : 'text',
							'placeholder' : 'Contenido del mensaje'
						}))
	to = forms.CharField(max_length=50,
					widget=forms.TextInput(attrs={
							'type' : 'email',
							'placeholder' : 'Destinatario'
						}))
	sender= forms.EmailField(widget=forms.TextInput(attrs={
							'type' : 'email',
							'placeholder' : 'Emisor'
						}))

	