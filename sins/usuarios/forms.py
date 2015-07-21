from django import forms
from django.contrib.auth.models import User
from perfis.models import Professor, Files, Cadeira, Curso
from django_enumfield import enum

class CadastrarUsuarioForm(forms.Form):

	first_name = forms.CharField(max_length=30, required=True)
	last_name = forms.CharField(max_length=30, required=True)
	course = forms.TypedChoiceField(choices=Curso.choices(), coerce=int)
	image = forms.ImageField(label='Selecione uma imagem.',required=False)
	username = forms.CharField(max_length=30, required=True)
	email = forms.EmailField(required=True)
	password = forms.CharField(required=True)

	def is_valid(self):
		resposta = True

		if not super(CadastrarUsuarioForm, self).is_valid():
			self.adiciona_erro("Verifique os dados informados")
			resposta = False

		email_ja_utilizado = User.objects.filter(email=self.data['email']).exists()

		if email_ja_utilizado:
			self.adiciona_erro("E-mail já utilizado")
			resposta = False
			
		if self.data['email'].startswith(' ') or self.data['email'].endswith(' '):
			self.adiciona_erro("E-mail começa ou termina com espaços em branco")
			resposta = False
		
		if self.data['username'].startswith(' ') or self.data['username'].endswith(' '):
			self.adiciona_erro("Nome de usuário começa ou termina com espaços em branco")
			resposta = False

		username_existe = User.objects.filter(username=self.data['username']).exists()

		if username_existe:
			self.adiciona_erro("Nome de usuário já em uso")
			resposta = False
			
		if '@' in self.data['username']:
			self.adiciona_erro("Nome de usuário inválido. Não pode possuir '@'")
			resposta = False

		return resposta

	def adiciona_erro(self, message):
		errors = self._errors.setdefault(forms.forms.NON_FIELD_ERRORS, forms.utils.ErrorList())
		errors.append(message)

class FilesForm(forms.Form):
	profs = forms.ModelChoiceField(Professor.objects.all(),label='Professor')
	name = forms.CharField(max_length=50,label='Nome do arquivo')
	desc = forms.CharField(max_length=100,label='Descrição')
	cadeira = forms.TypedChoiceField(choices=Cadeira.choices(), coerce=int)
	docfile = forms.FileField(label='Selecione um arquivo.',help_text='max. 42 megabytes')