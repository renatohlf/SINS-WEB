from django.contrib import admin
from .models import Professor, Files,Painel

# Register your models here.


class FilesAdmin(admin.ModelAdmin):
	list_display = ('name','desc','prof','docfile','pub_date')
	fields = ['user','prof','name','desc','docfile']
admin.site.register(Files,FilesAdmin)


class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('name','reg')
	fields = ['name','reg']
admin.site.register(Professor,ProfessorAdmin)

class PainelAdmin(admin.ModelAdmin):
	list_display = ('title','desc','image')
	fields = ['title', 'desc', 'image']
	
admin.site.register(Painel,PainelAdmin)
