# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0003_delete_painel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Painel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(verbose_name='Título', max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
