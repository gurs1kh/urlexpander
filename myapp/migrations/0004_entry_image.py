# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150808_1545'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.CharField(max_length=2083, default='a'),
            preserve_default=False,
        ),
    ]
