# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-12 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20160712_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='logo',
            field=models.ImageField(upload_to=''),
        ),
    ]