# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-26 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('legacy', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='DirectedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('legacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='legacy.LegacyModel')),
            ],
        ),
    ]