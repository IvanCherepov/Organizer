# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(verbose_name=b'date_created')),
                ('date_modified', models.DateTimeField(verbose_name=b'date_modified')),
            ],
            options={
                'ordering': ['date_modified'],
                'verbose_name': 'list',
                'verbose_name_plural': 'lists',
            },
        ),
        migrations.RemoveField(
            model_name='link',
            name='date_updated',
        ),
        migrations.RemoveField(
            model_name='link',
            name='title',
        ),
        migrations.AddField(
            model_name='link',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 28, 5, 48, 10, 22743, tzinfo=utc), verbose_name=b'date_modified'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='name',
            field=models.CharField(default='temp', max_length=50, verbose_name=b'name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='date_created',
            field=models.DateTimeField(verbose_name=b'date_created'),
        ),
        migrations.AddField(
            model_name='list',
            name='links',
            field=models.ManyToManyField(to='organizer.Link'),
        ),
        migrations.AddField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(related_name='lists', verbose_name=b'owner', to='organizer.UserProfile'),
        ),
    ]
