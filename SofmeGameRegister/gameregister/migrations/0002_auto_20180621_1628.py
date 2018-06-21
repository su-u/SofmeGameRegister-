# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gameregister', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameInfo',
            fields=[
                ('name', models.CharField(verbose_name='名前', max_length=255, help_text='255文字以下')),
                ('id', models.IntegerField(verbose_name='id', primary_key=True, default=0, serialize=False, help_text='0~50')),
                ('discription', models.TextField()),
                ('gamefile', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='FileNameModel',
        ),
    ]
