# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-29 12:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200529_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
