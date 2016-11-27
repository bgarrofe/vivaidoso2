# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 20:43
from __future__ import unicode_literals

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('vivaidoso', '0008_auto_20161123_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='faixa_valor',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, b'Gratuito'), (2, b'At\xc3\xa9 R$ 1.000'), (3, b'R$ 1.000 a 3.000'), (4, b'R$ 3.000 a 5.000'), (5, b'R$ 5.000 a 7.000'), (6, b'R$ 7.000 a 10.000')], default=1, max_length=11),
        ),
    ]