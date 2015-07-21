# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0013_auto_20150720_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='image',
            field=models.ImageField(blank=True, upload_to='perfil_image/', default='/static/perfis/images/avatar.png'),
        ),
    ]
