# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0005_auto_20150704_2204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='files',
            old_name='files',
            new_name='docfile',
        ),
    ]
