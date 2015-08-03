from django.db import models
from django.contrib.auth.models import User
from django_enumfield import enum
from django.templatetags.static import static
# Create your models here.


class Curso(enum.Enum):
	NONE = 0
	ECOMP = 1
	CIV = 2
	TELECOM = 3
	ELETRI = 4
	ELETRO = 5
	MECAN = 6
	MECAT = 7
	
	labels = {
		NONE: 'vazio',
		ECOMP: 'ECOMP',
		CIV: 'Civil',
		TELECOM: 'Telecomunicações',
		#...
	}
	
class Cadeira(enum.Enum):
	NONE = 0
	CALC1  = 1
	CALC2 = 2
	CALC3 = 3
	CALC4 = 4 
	CALC_NUM = 5
	ALGEBR_L = 6
	GEO_ANAL = 7
	LPI = 9
	LPO = 10
	ED = 11
	#...
	labels = {
        NONE: 'vazio',
        CALC1: 'Calculo 1',
		CALC2: 'Calculo 2',
		CALC3: 'Calculo 3',
		#...
    }
	

class Professor(models.Model):
	name = models.CharField(max_length=50, null=False)
	reg = models.IntegerField(null=False)
	user = models.OneToOneField(User, null=False, default=None)
	image = models.ImageField(upload_to='perfil_image/', blank=True, default=static('perfis/images/avatar.png'))
	
	@property 
	def first_name(self):
		return self.user.first_name

	@property
	def last_name(self):
		return self.user.last_name

	@property 
	def username(self):
		return self.user.username

	@property 
	def email(self):
		return self.user.email

	def __str__(self):
		return self.name

class Perfil(models.Model):
	user = models.OneToOneField(User)
	curso = enum.EnumField(Curso, default=Curso.NONE)
	image = models.ImageField(upload_to='perfil_image/', blank=True, default=static('perfis/images/avatar.png'))
	
	@property 
	def full_name(self):
		return self.user.get_full_name()

	@property 
	def first_name(self):
		return self.user.first_name

	@property
	def last_name(self):
		return self.user.last_name

	@property 
	def username(self):
		return self.user.username

	@property 
	def email(self):
		return self.user.email
		
	def __str__(self):
		return self.user.username

class Files(models.Model):
	#nome do professor responsavel pelo arquivo. ou arquivo nomeado com nome deste professor
	user = models.ForeignKey(Perfil,blank=True,default=1)
	#nome do professor no qual o arquivo pertence
	prof = models.ForeignKey(Professor)
	#nome do arquivo
	name = models.CharField(max_length=50)
	#descrição do arquivo
	desc = models.CharField(max_length=100,blank=True)
	#cadeira a ser publicada
	cadeira = enum.EnumField(Cadeira, default=Cadeira.NONE)
	#numero de comentarios
	n_comments = models.IntegerField(default=0)
	#votos
	rating = models.IntegerField(default=0)
	#arquivo a ser salvo
	docfile = models.FileField(upload_to='files/')
	#data de publicação
	pub_date = models.DateTimeField('date published',auto_now_add=True,blank=True)
	#curso a ser destinado o arquivo
	curso = enum.EnumField(Curso, default=Curso.NONE)
	
	#retorna o nome do arquivo
	def __str__(self):
		return self.name
		

class Painel(models.Model):
	title = models.CharField(max_length=50, verbose_name='Título')
	desc = models.CharField(max_length=50)
	image = models.ImageField()
	
	def __str__(self):
		return self.title
	
class Questions(models.Model):
	title = models.CharField()
	desc = models.CharField()
	rating = models.IntegerField(default=0)
	
