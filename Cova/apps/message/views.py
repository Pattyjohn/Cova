from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import *
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView
from .forms import EmailForm
from .models_user import User
# Create your views here.


class Email(FormView):
	form_class = EmailForm
	template_name = 'message/email.html'
# Create your views here.
	
	success_url=reverse_lazy('main:home')

	def get_context_data(self, **kwargs):
		context=super(Email, self).get_context_data(**kwargs)
		context['users'] = User.objects.all()
		context['medical'] = User.objects.filter(is_medical=True)
		context['patient'] = User.objects.filter(is_patient=True)
		return context
		

	def form_valid(self, form):
		
		subject = form.cleaned_data['subject']
		message = form.cleaned_data['message']
		sender = form.cleaned_data['sender']
		cc_myself = form.cleaned_data['cc_myself']

		recipients = ['info@example.com']
		if cc_myself:
			recipients.append(sender)

		send_mail(subject, message, sender, recipients)
		
