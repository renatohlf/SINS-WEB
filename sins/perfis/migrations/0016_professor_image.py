# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0015_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='image',
            field=models.ImageField(blank=True, upload_to='perfil_image/', default='/static/perfis/images/avatar.png'),
        ),
    ]
