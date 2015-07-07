# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=100)),
                ('files', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Painel',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('reg', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='files',
            name='prof',
            field=models.ForeignKey(to='perfis.Professor'),
        ),
    ]
