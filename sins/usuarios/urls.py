from django.conf.urls import include, url
from usuarios.views import CadastrarUsuarioView, LoginView, success, logout_view

urlpatterns = [
	url(r'^cadastro/$', CadastrarUsuarioView.as_view(), name='cadastrar'),
	url(r'^success/(?P<name>.+)/(?P<username>.+)$', success, name='cadastro_sucedido'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view, name='logout')
]