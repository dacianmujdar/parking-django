# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-12 17:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0002_auto_20180611_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='creator',
            field=models.ForeignKey(help_text=b'The user which created the offer', on_delete=django.db.models.deletion.CASCADE, related_name='own_offers', to='account.Account'),
        ),
    ]
