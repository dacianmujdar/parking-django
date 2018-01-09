# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-09 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0002_auto_20180109_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(help_text='The request type', max_length=128, verbose_name='Request type')),
            ],
        ),
    ]
