# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0010_auto_20150709_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='curso',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='files',
            name='n_comments',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='rating',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files',
            name='cadeira',
            field=models.IntegerField(default=0),
        ),
    ]
