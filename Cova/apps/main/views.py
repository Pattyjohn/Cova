from django.shortcuts import render
from django.views.generic import TemplateView
from .models_user import User
# Create your views here.


class Home(TemplateView):

	template_name = 'main/home.html'

	def get_context_data(self, **kwargs):
		context=super(Home, self).get_context_data(**kwargs)
		context['users'] = User.objects.all()
		context['medical'] = User.objects.filter(is_medical=True)
		context['patient'] = User.objects.filter(is_patient=True)
		
		return context
		