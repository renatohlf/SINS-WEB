from django.conf.urls import include, url
from perfis import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^files/$', views.FilesView.as_view(), name='files'),
    url(r'^upload/$', login_required(views.FilesUploadView.as_view()), name='upload'),
    url(r'^sucess/$', login_required(views.FilesIndexView.as_view()), name='sucess'),
    url(r'^perfil/$', views.exibir_perfil, name='exibir_perfil')
]
