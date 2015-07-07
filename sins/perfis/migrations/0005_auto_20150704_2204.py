# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0004_painel'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='user',
            field=models.ForeignKey(to='perfis.Perfil', blank=True, default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files',
            name='desc',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='files',
            field=models.FileField(upload_to='files/'),
        ),
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='prof',
            field=models.ForeignKey(to='perfis.Professor', blank=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]
