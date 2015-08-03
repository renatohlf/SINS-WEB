# -*- coding: UTF-8 -*-

from django.shortcuts import render, redirect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.views import generic
from django.contrib.auth.models import User, AnonymousUser
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from django_enumfield import enum
from usuarios.forms import FilesForm
from .models import Files, Professor, Perfil, Painel, Cadeira


class BaseMixin(object):
	def get_perfil(self):
		perfil = get_perfil_logado(self.request)
		return perfil
	
	def get_context_data(self, **kwargs):
		ctx = super().get_context_data(**kwargs)
		ctx['perfil_logado'] = self.get_perfil()
		return ctx

class ArtigosView(BaseMixin, generic.ListView):
	model = Files
	template_name = 'artigos.html'
	context_object_name = 'file_list'
	queryset = Files.objects.all()
	paginate_by=5 
	
	 
	def get_queryset(self):
		return Files.objects.order_by('-pub_date')



class FilesView(BaseMixin, generic.ListView):
	model = Files
	template_name = 'files.html'
	context_object_name = 'file_list'
	queryset = Files.objects.all()
	paginate_by=5 
	
	 
	def get_queryset(self):
		return Files.objects.order_by('-pub_date')

def download_view(request):
		
	# Create the HttpResponse object with the appropriate PDF headers.
	#import pdb; pdb.set_trace();
	filename = request.GET.get('nome_arq').split('/')[-1]
	obj = Files.objects.filter(name=filename)
	response = HttpResponse(obj[0].docfile, content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=%s' % obj[0].docfile.url.split('/')[-1]
		
	return response


#Página de informações
class InfoView(BaseMixin,generic.ListView):
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



class ExibirPerfilView(BaseMixin ,generic.View):
	
	def default_return(self, request, requested_user):
		is_it_prof = is_prof(request, requested_user)
		logged_is_prof = is_prof(request, request.user)
		perfil = None
		
		if requested_user.is_superuser:
			try:
				perfil = Perfil.objects.get(user=requested_user)
			except Perfil.DoesNotExist:
				perfil = Perfil(user=requested_user)
				perfil.save()
		elif is_it_prof:
			perfil = Professor.objects.get(user=requested_user)
		else:
			try:
				perfil = Perfil.objects.get(user=requested_user)
			except Perfil.DoesNotExist:
				pass
		
		return render(request, 'perfil.html', {'requested_user' : requested_user, 'is_prof' : is_it_prof, 'logged_is_prof' : logged_is_prof, 'perfil':perfil, 'perfil_logado': get_perfil_logado(request)})
			
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, username):
		if request.user is not None and not isinstance(request.user, AnonymousUser):
			requested_user = User.objects.get(username=username)
			
			is_it_prof = is_prof(request, requested_user)
			
			if requested_user.is_superuser:
				try:
					perfil = Perfil.objects.get(user=requested_user)
				except Perfil.DoesNotExist:
					perfil = Perfil(user=requested_user)
					perfil.save()
			elif is_it_prof:
				perfil = Professor.objects.get(user=requested_user)
			else:

				perfil = Perfil.objects.get(user=requested_user)			
			
			return self.default_return(request, requested_user)
		else:
			return redirect('login')
	
	def post_avatar(self, request, requested_user):
		img = request.FILES.get('new_avatar', None)
		user = request.user
		perfil = None
		
		if is_prof(request, user):
			perfil = Professor.objects.get(user=user)
		else:
			perfil = Perfil.objects.get(user=user)
			
		perfil.image = img
		perfil.save()
			
		return self.default_return(request, requested_user)

	def post_edition(self, request, requested_user):
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		user = request.user
		
		if first_name == '' or last_name == '':
			pass
		else:
			user.first_name = first_name
			user.last_name = last_name
			user.save()
		
		return self.default_return(request, requested_user)
		
	def post_search(self, request, requested_user):
		query = request.POST['search-field'].lower()
		all_profs = Professor.objects.all()
		list_all = []
		
		for each_one in all_profs:
			full_name = each_one.user.get_full_name().lower()
			if full_name in query:
				list_all.append(each_one)
				continue
			if query in full_name:
				list_all.append(each_one)
				continue
			if each_one.username.lower() in query:
				list_all.append(each_one)
				continue
			if each_one.email in query:
				list_all.append(each_one)
				continue
			#fazer o if das tags
		
		return render(request, 'search.html', {'perfil': get_perfil_logado(request), 'lista': list_all})
	
	def post(self, request, username):
		requested_user = User.objects.get(username=username)
		perfil = get_perfil_logado(request)
		if request.POST['post_type'] == 'avatar':
			return self.post_avatar(request, requested_user)
		elif request.POST['post_type'] == 'edit':
			return self.post_edition(request, requested_user)
		elif request.POST['post_type'] == 'search':
			return self.post_search(request, requested_user)
		else:

			return self.default_return(request, requested_user)
		

def is_prof(request, user):
	try:
		possible_prof = Professor.objects.get(user_id=user.id)
		return True
	except Professor.DoesNotExist:
		return False
	
def get_perfil_logado(request):
	user = User.objects.get(username=request.user.username, email=request.user.email)
	#import pdb; pdb.set_trace();
	if user.is_authenticated():
		try:
			perfil = None
			if is_prof(request, user):
				perfil = Professor.objects.get(user=user)
			else:
				perfil = Perfil.objects.get(user=user)
			print('%s', perfil.user.get_full_name())
		except:	
			print('Perfil não encontrado')
		return perfil
	else:
		return None
		
class FilesUploadView(BaseMixin, generic.FormView):

	template_name = 'upload.html'
	form_class = FilesForm
	
	def form_valid(self, form):
		
		#import pdb; pdb.set_trace()
		docfile = Files(
			prof= Professor.objects.get(id=self.get_form_kwargs().get('data')['profs']),
			name= self.get_form_kwargs().get('data')['name'],
			desc= self.get_form_kwargs().get('data')['desc'],
			cadeira =self.get_form_kwargs().get('data')['cadeira'], 
			docfile=self.get_form_kwargs().get('files')['docfile'])
		docfile.save()
		self.id = docfile.id
		
		
	def post(self, request):
		super().post(request)
		return redirect("files")
	

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def donate(request):
	perfil = get_perfil_logado(request)
	return render(request, 'donate.html', {'perfil_logado':perfil})

#Vote method, método para votação, testando..
#a implementação provalvelmente precisará do uso de ajax, ou javascript.
def vote(request, files_id):
	p = get_object_or_404(Files, pk=files_id)
	selected_choice = p.choice_set.get(pk=request.POST['choice'])
	
	def like():
		selected_choice.votes += 1
		selected_choice.save()
		
	def unlike():
		selected_choice.votes -= 1
		selected_choice.save()
		
	options = { 0 : like, 1 : unlike, }
	#options[0]() defina qual o numero no colchetes, e será a escolha do voto.
		   