from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from usuarios.forms import CadastrarUsuarioForm
from perfis.models import Perfil
from perfis.views import get_perfil_logado
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control

class CadastrarUsuarioView(View):

	template_name = 'cadastro.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		return render(request, self.template_name)
		
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def post(self, request):
		form = CadastrarUsuarioForm(request.POST)

		if form.is_valid():

			new_user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
			new_user.first_name = form.data['first_name']
			new_user.last_name = form.data['last_name']
			new_user.save()

			perfil = Perfil(user=new_user)
			perfil.save()

			return redirect('cadastro_sucedido', name=perfil.first_name, username=perfil.username)

		return render(request, self.template_name, {'form': form})


class LoginView(View):

	template_name = 'login.html'

	def auth(self, name, password):
		if '@' in name:
			try:
				user = User.objects.get(email=nome)
				return authenticate(username=user.username, password=password)

			except User.DoesNotExist:
				return None
		else:
			return authenticate(username=name, password=password)

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		next_url = ''
		
		if 'next' in request.GET:
			next_url = request.GET['next']
		else:
			next_url = 'exibir_perfil'
			
		return render(request, self.template_name, {'next_url':next_url})

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def post(self, request):
		name = request.POST['username']
		password = request.POST['password']
		
		user = self.auth(name, password)
		
		if user is not None:
			login(request, user)
			perfil = get_perfil_logado(request)
			print('Login no perfil de username ' + perfil.username)
			
			return redirect(request.POST['next_url'])
			
		else:
			error_list = True
			print('Login falhou')
			return render(request, self.template_name, {'error_list':error_list})


def success(request, name, username):
	try:
		user = User.objects.get(first_name=name, username=username)
		return render(request, 'success.html', {'name': name, 'username': username})
	except User.DoesNotExist:
		return redirect('index')
	
