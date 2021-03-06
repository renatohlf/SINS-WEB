from django.conf.urls import include, url
from perfis import views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^donate/$', views.donate, name='donate'),    
    url(r'^files/$', views.FilesView.as_view(), name='files'),
    url(r'^files/download/', views.download_view, name='downloads'),
    url(r'^upload/$', login_required(views.FilesUploadView.as_view()), name='upload'),
    url(r'^perfil/(?P<username>.+)$', views.ExibirPerfilView.as_view(), name='exibir_perfil'),
    url(r'^info/$', views.InfoView.as_view(), name='info'),
    url(r'^artigos/$', views.ArtigosView.as_view(), name='artigos')
    
]
