# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileNameModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('file_name', models.CharField(max_length=50)),
                ('upload_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
