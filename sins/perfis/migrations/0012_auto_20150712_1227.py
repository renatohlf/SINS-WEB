# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0011_auto_20150712_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='n_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='files',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
