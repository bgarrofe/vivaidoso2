# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-28 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivaidoso', '0011_auto_20161126_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='tipo',
            field=models.IntegerField(choices=[(1, b'Casas de Repouso'), (2, b'Apoio Domiciliar'), (3, b'Home Care'), (4, b'Centro Dia')], default=1),
        ),
    ]
