# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150804_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='date',
        ),
        migrations.AddField(
            model_name='entry',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
