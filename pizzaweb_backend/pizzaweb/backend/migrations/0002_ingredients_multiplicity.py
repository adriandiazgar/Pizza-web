# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-16 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredients',
            name='multiplicity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]