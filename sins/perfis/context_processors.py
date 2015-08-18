from perfis.views import get_perfil_logado, is_prof

def perfil_logado_processor(request):
	perfil = get_perfil_logado(request)
	logged_is_prof = is_prof(request, request.user)
	return {'perfil_logado': perfil, 'logged_is_prof' : logged_is_prof}