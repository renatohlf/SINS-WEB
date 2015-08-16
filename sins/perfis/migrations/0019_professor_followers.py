# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0018_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='followers',
            field=models.ManyToManyField(to='perfis.Perfil'),
        ),
    ]
