# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estore', '0002_auto_20151028_2359'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='event_date',
        ),
    ]
