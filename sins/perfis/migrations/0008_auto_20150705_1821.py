# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0007_auto_20150705_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='user',
            field=models.ForeignKey(blank=True, default=1, to='perfis.Perfil'),
        ),
    ]
