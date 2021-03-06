# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-23 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Isotopic_labeling', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('Isotopic_labeling_details', models.CharField(blank=True, max_length=20)),
                ('Nb_factors', models.IntegerField(default=0)),
                ('Factor_name_lst', models.CharField(max_length=120, null=True)),
                ('Nb_samples', models.IntegerField(default=1)),
                ('Generic_Sample_Name', models.CharField(max_length=120)),
                ('Sample_Name', models.CharField(max_length=120, null=True)),
            ],
        ),
    ]
