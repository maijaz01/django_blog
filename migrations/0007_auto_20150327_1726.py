# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150327_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.IntegerField(default=None),
            preserve_default=True,
        ),
    ]
