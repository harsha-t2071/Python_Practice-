# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-10-29 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquiryform_app', '0002_auto_20191029_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquirydata',
            name='mobile',
            field=models.IntegerField(max_length=10),
        ),
    ]