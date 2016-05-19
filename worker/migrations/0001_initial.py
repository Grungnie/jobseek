# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=256)),
                ('heading', models.CharField(max_length=256)),
                ('work_type', models.CharField(max_length=256)),
                ('classification', models.CharField(max_length=256)),
                ('sub_classification', models.CharField(max_length=256)),
                ('address_locality', models.CharField(max_length=265)),
                ('address_region', models.CharField(max_length=265)),
                ('body', models.TextField()),
            ],
        ),
    ]
