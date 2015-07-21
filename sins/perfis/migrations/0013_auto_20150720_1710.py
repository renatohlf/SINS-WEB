# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0012_auto_20150712_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='curso',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='files',
            name='prof',
            field=models.ForeignKey(to='perfis.Professor'),
        ),
    ]
