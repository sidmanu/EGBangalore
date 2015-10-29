# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0003_auto_20151029_0013'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='detail',
            new_name='event_detail',
        ),
        migrations.AddField(
            model_name='event',
            name='event_short',
            field=models.CharField(default=b'', max_length=300),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='map_url',
            field=models.CharField(default=b'invalid', max_length=200),
            preserve_default=True,
        ),
    ]
