# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0009_auto_20150709_1055'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='cadeira',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
