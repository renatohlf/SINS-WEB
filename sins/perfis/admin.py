from django.contrib import admin
from .models import Professor, Files,Painel

# Register your models here.


class FilesAdmin(admin.ModelAdmin):
	list_display = ('name','desc','cadeira','n_comments','rating','docfile','pub_date','curso')
	fields = ['curso','prof','cadeira','name','desc','docfile']
admin.site.register(Files,FilesAdmin)


class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('user','name','reg')
	fields = ['user','name','reg']
admin.site.register(Professor,ProfessorAdmin)

class PainelAdmin(admin.ModelAdmin):
	list_display = ('title','desc','image')
	fields = ['title', 'desc', 'image']
	
admin.site.register(Painel,PainelAdmin)
