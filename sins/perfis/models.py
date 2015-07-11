from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Professor(models.Model):
	name = models.CharField(max_length=50, null=False)
	reg = models.IntegerField(null=False)
	user = models.OneToOneField(User, null=False, default=None)

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
	prof = models.ForeignKey(Professor, blank=True)
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=100,blank=True)
	cadeira = models.CharField(max_length=50)
	docfile = models.FileField(upload_to='files/')
	pub_date = models.DateTimeField('date published',auto_now_add=True,blank=True)
	
	def __str__(self):
		return self.name

class Painel(models.Model):
	title = models.CharField(max_length=50, verbose_name='Título')
	desc = models.CharField(max_length=50)
	image = models.ImageField()
	
	def __str__(self):
		return self.title
	
	
	
