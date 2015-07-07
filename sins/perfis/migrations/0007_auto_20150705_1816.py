# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0006_auto_20150705_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='prof',
            field=models.ForeignKey(to='perfis.Professor', default=1, blank=True),
        ),
    ]
