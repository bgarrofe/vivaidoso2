# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 01:55
from __future__ import unicode_literals

from django.db import migrations, models
import vivaidoso.utils


class Migration(migrations.Migration):

    dependencies = [
        ('vivaidoso', '0007_uploadfile_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file',
            field=models.FileField(upload_to=vivaidoso.utils.upload_path_handler),
        ),
    ]
