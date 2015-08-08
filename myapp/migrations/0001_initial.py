# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('short_url', models.CharField(max_length=2083)),
                ('long_url', models.CharField(max_length=2083)),
                ('status', models.CharField(max_length=3)),
                ('title', models.TextField()),
                ('date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
