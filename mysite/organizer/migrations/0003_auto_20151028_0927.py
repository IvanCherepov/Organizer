# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0002_auto_20151028_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='owner',
            field=models.ForeignKey(related_name='links', verbose_name=b'owner', to='organizer.UserProfile'),
        ),
    ]
