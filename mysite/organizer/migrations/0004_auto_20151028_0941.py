# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0003_auto_20151028_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(related_name='links', verbose_name=b'owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='list',
            name='owner',
            field=models.ForeignKey(related_name='lists', verbose_name=b'owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
