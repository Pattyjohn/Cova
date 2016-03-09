from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import login, logout, authenticate

from .forms import UserLoginForm, UserCreateForm
# Create your views here.

def LogOut(request):
	logout(request)
	return redirect(reverse('main:home'))



class LogInView(FormView):

	template_name= 'users/login.html'
	form_class = UserLoginForm
	success_url=reverse_lazy('main:home')

	def form_valid(self, form):
		user = authenticate(
				username = form.cleaned_data['username'],
				password = form.cleaned_data['password']
					)
		if user.is_active:
			login(self.request, user)
			return super(LogInView, self).form_valid(form)
		else:
			return redirect(reverse('main:not_access'))




class UserRegisterView(CreateView):

	form_class = UserCreateForm
	template_name= 'users/register.html'
	success_url=reverse_lazy('users:login')

	def form_valid(self,form):
		user = form.save()
		user.set_password(form.cleaned_data['password'])
		return super(UserRegisterView,self).form_valid(form)