# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0002_auto_20150703_1505'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Painel',
        ),
    ]
