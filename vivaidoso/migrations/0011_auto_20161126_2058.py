# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 22:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vivaidoso', '0010_auto_20161126_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='dependencia',
            field=models.IntegerField(choices=[(1, b'Grau 1'), (2, b'Grau 2'), (3, b'Grau 3')], default=1),
        ),
    ]
