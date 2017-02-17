# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-02-16 23:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Publicaciones', '0005_auto_20170216_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publish', to=settings.AUTH_USER_MODEL),
        ),
    ]
