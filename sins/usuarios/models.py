#from django.db import models
#from django.db.models.signals import post_save

#def cria_user_perfil(sender, instance, created, **kwargs):
#    if created:
#        player = Perfil.objects.create(user=instance)
#
#post_save.connect(cria_user_player, sender=User)