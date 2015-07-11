# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views import generic
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from usuarios.forms import FilesForm
from .models import Files, Professor, Perfil, Painel


class FilesView(generic.ListView):
	model = Files
	template_name = 'files.html'
	context_object_name = 'file_list'
	queryset = Files.objects.all()
	paginate_by=5 
	
	 
	def get_queryset(self):
		return Files.objects.order_by('-pub_date')

#Página de informações
class InfoView(generic.ListView):
	#Carrega a table do Painel
	model = Painel
	#nome da página
	template_name = 'info.html'
	#carrega os objetos em uma lista, para ser consumida na página
	context_object_name = 'painel_list'
	
	def get_queryset(self):
		#retorna a lista por ordem de título. obs:title é um campo da tabela Painel
		return Painel.objects.order_by('-title')
		
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
	return render(request, 'index.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def exibir_perfil(request):
	return render(request, 'perfil.html')

def get_perfil_logado(request):
	user = User.objects.get(username=request.user.username, email=request.user.email)
	if user.is_authenticated():
		perfil = Perfil.objects.get(user=user)
		print('%s', perfil.full_name)
		return perfil
	else:
		return None

	
class FilesUploadView(generic.FormView):
	template_name = 'upload.html'
	form_class = FilesForm

	def form_valid(self, form):
		import pdb; pdb.set_trace()
		docfile = Files(
			prof= Professor.objects.get(id=self.get_form_kwargs().get('data')['profs']),
			name= self.get_form_kwargs().get('data')['name'],
			desc= self.get_form_kwargs().get('data')['desc'],
			cadeira = self.get_form_kwargs().get('data')['cadeira'], 
			docfile=self.get_form_kwargs().get('files')['docfile'])
		docfile.save()
		self.id = docfile.id
		print('Fail!')
		
	def post(self, request):
		print('Sucesso!')
		return redirect("files")
		
	
	
