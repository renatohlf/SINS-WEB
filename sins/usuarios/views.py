from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from usuarios.forms import CadastrarUsuarioForm
from perfis.models import Perfil, Professor
from perfis.views import get_perfil_logado
from django.http import HttpResponseRedirect
from django.views.decorators.cache import cache_control
from django.templatetags.static import static

#View para cadastro
class CadastrarUsuarioView(View):
	
	#Define uma variável com o nome do template da página
	template_name = 'cadastro.html'

	#O get apenas mostra a página a partir de uma requisição
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		form = CadastrarUsuarioForm
		return render(request, self.template_name, {'form': form })
		
	#O post vai verificar os dados e cadastrar caso sejam dados válidos
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def post(self, request):
		#Passa os dados para o form e verifica a validade dos dados pelo método is_valid()
		form = CadastrarUsuarioForm(request.POST)
		#import pdb; pdb.set_trace();
		if form.is_valid():
			
			#Cria um novo usuário com os dados obtidos e persiste
			new_user = User.objects.create_user(form.data['username'], form.data['email'], form.data['password'])
			new_user.first_name = form.data['first_name']
			new_user.last_name = form.data['last_name']
			new_user.save()
			#seta o campo curso escolhido pelo usuario no form
			course = form.data['course']
			#pega a imagem que o usuário escolheu no form
			img = request.FILES.get('image',None)
			
			
			#Cria a variavel perfil para uso posterior
			perfil = None

			#Verifica se há o campo user_type na emissão dos dados.
			#Isso só irá acontecer caso o cadastro tenha sido realizado por um superuser
			if 'user_type' in request.POST:
				#Verifica se é um professor cadastrado. Se sim, cria o professor e persiste. Loga no console
				if request.POST['user_type'] == 'professor':
					professor = Professor(name=new_user.get_full_name(), reg=request.POST['reg'], user=new_user)
					perfil = professor
					professor.save()
					print('Superuser cadastrou um professor. Username: ' + new_user.username)
				#Caso não seja um professor, é um perfil comum. Loga no console
				else:
					perfil = Perfil(user=new_user, curso=course, image=img)
					perfil.save()
					print('Superuser cadastrou um perfil. Username: ' + new_user.username)
			#Esse else representa um cadastro comum, ou seja, um perfil. Loga no console
			else:
				perfil = Perfil(user=new_user, curso=course, image=img)
				perfil.save()
				print('Cadastro ordinário. Username: ' + new_user.username)
				
			#Redireciona para a página de sucesso do cadastro
			return redirect('cadastro_sucedido', name=perfil.first_name, username=perfil.username)
			
		#Gera novamente a página de cadastro passando o form contendo os erros
		return render(request, self.template_name, {'form': form })
		


#View responsável pelo login
class LoginView(View):

	#Variável com o nome do template da página
	template_name = 'login.html'

	#Função de autenticação pelo email ou por username.
	def auth(self, name, password):
		#verifica se o name é um email. Se sim, procura o usuário pelo email.
		if '@' in name:
			try:
				user = User.objects.get(email=name)
				return authenticate(username=user.username, password=password)

			except User.DoesNotExist:
				#caso não exista users com o email fornecido, retorna None
				return None
		#Caso seja um username, apenas usa o authenticate
		else:
			return authenticate(username=name, password=password)

    #Verifica se houve requisição de um redirecionamento e salva na página. E renderiza
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		next_url = ''
		
		if 'next' in request.GET:
			next_url = request.GET['next']
		else:
			next_url = 'exibir_perfil'
		#import pdb; pdb.set_trace();
		return render(request, self.template_name, {'next_url':next_url})

	#Obtém os dados da página e tenta fazer o login
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def post(self, request):
		name = request.POST['username']
		password = request.POST['password']
		
		user = self.auth(name, password)

		#Se existe o usuário com os dados, faz o login. Loga no console. Redireciona para a página devida
		if user is not None:
			login(request, user)
			print('Login - username: ' + request.user.username)
			
			next_url = request.POST['next_url']
			
			if not next_url: 
				next_url= 'exibir_perfil' 
			return redirect(next_url)
				
		#Mostra os erros do login renderizando a página de login novamente
		else:
			error_list = True
			print('Login falhou')
			
			return render(request, self.template_name, {'error_list':error_list})


#Função de view da página de cadastro bem sucedido
def success(request, name, username):
	try:
		user = User.objects.get(first_name=name, username=username)
		return render(request, 'success.html', {'name': name, 'username': username})
	except User.DoesNotExist:
		return redirect('index')
	
