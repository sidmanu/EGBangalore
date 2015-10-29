# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookTestimonial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('book', models.ForeignKey(to='estore.Book')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('detail', models.TextField()),
                ('image_url', models.CharField(default=b'invalid', max_length=100)),
                ('date', models.DateTimeField()),
                ('keywords', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('arrival_date', models.DateTimeField()),
                ('quantity', models.IntegerField()),
                ('book', models.ForeignKey(to='estore.Book')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(unique=True, max_length=500),
        ),
    ]
