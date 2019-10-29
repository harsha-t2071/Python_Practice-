# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-25 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('salary', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
    ]
