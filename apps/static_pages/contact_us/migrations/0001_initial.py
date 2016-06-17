# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-16 08:08
from __future__ import unicode_literals

import apps.static_pages.contact_us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, validators=[apps.static_pages.contact_us.models.validate_even])),
                ('last_name', models.CharField(max_length=50, validators=[apps.static_pages.contact_us.models.validate_even])),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]