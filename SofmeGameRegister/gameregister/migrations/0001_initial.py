# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gameregister.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('game_id', gameregister.models.IntegerRangeField(verbose_name='id', default=1, help_text='1~100')),
                ('name', models.CharField(verbose_name='名前', max_length=100, help_text='100文字以下')),
                ('representative', models.CharField(verbose_name='企画者', max_length=100, blank=True, help_text='100文字以下')),
                ('discription', models.TextField()),
                ('gamefile', models.FileField(blank=True, upload_to='gamefile')),
                ('panel', models.FileField(blank=True, upload_to='panel')),
                ('movie', models.FileField(blank=True, upload_to='movie')),
            ],
        ),
    ]
