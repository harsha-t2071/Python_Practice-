# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-29 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryform_app', '0004_auto_20191029_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquirydata',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
