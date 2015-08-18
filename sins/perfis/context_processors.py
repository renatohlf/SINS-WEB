from perfis.views import get_perfil_logado, is_prof
from django.contrib.auth.models import AnonymousUser

def perfil_logado_processor(request):
	if request.user is not None and not isinstance(request.user, AnonymousUser):
		perfil = get_perfil_logado(request)
		logged_is_prof = is_prof(request, request.user)
		return {'perfil_logado': perfil, 'logged_is_prof' : logged_is_prof}
	else:
		return []