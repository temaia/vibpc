# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-21 14:18
from __future__ import unicode_literals

from django.conf import settings
import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_summary', models.TextField(max_length=300)),
                ('Project_keywords', models.CharField(max_length=120)),
                ('Affiliation', models.CharField(max_length=120)),
                ('Address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Issue', models.CharField(blank=True, max_length=200)),
                ('Name', models.CharField(max_length=120)),
                ('Study_Type', models.CharField(choices=[('VIB', 'VIB'), ('Academic', 'Academic'), ('Non-Academic', 'Non Academic')], max_length=50)),
                ('Group_Leader', models.CharField(max_length=120)),
                ('Analysis_Type', models.CharField(choices=[('shotgun', 'Shotgun analysis'), ('APMS', 'Affinity-Purification MS (AP-MS)'), ('PTMs', 'PTM analysis'), ('gelband', 'Protein gel band analysis'), ('proteinmass', 'Protein mass determination'), ('other', 'Other')], max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Specimen_APMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Bait_Molecule', models.BooleanField(choices=[(True, 'a protein'), (False, 'another type of molecule')])),
                ('IPAntibodies_names', models.CharField(max_length=120)),
                ('IPAntibodies_Supplier', models.CharField(max_length=120)),
                ('IPAntibodies_CatalogNumber', models.CharField(max_length=120)),
                ('Species', models.CharField(max_length=120)),
                ('Taxon_id', models.CharField(max_length=120)),
                ('Sequence_Database_Public_Availability', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('Sequence_Database_Source', models.BooleanField()),
                ('Sequence_Database_File', models.FileField(upload_to=b'')),
                ('Sample_Type', models.BooleanField(choices=[(True, 'washed beads'), (False, 'eluate')], max_length=50)),
                ('Sample_Vial', models.CharField(max_length=120)),
                ('Buffer_Composition', models.CharField(max_length=300)),
                ('Volume', models.FloatField()),
                ('VUnit', models.BooleanField(choices=[(True, '\u03bcl'), (False, 'ml')])),
                ('Protein_Concentration', models.FloatField()),
                ('CUnit', models.CharField(choices=[('nmol/ul', 'nmol/\u03bcl'), ('umol/ul', '\u03bcmol/\u03bcl'), ('mmol/ul', 'mmol/\u03bcl')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Specimen_GB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Experimental_Setup_Sample_Preparation', models.TextField(max_length=300)),
                ('Gel_GelBand_Image', models.FileField(upload_to=b'')),
                ('Species', models.CharField(max_length=120)),
                ('Taxon_id', models.CharField(max_length=120)),
                ('Sequence_Database_Public_Availability', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('Sequence_Database_Source', models.BooleanField()),
                ('Sequence_Database_File', models.FileField(upload_to=b'')),
                ('Gel_Type', models.TextField(max_length=300)),
                ('Gel_Supplier', models.CharField(max_length=120)),
                ('Gel_CatalogNumber', models.CharField(max_length=120)),
                ('Gel_Staining_Method', models.CharField(max_length=120)),
                ('Electrophoresis_Type', models.BooleanField(choices=[(True, 'SDS-PAGE'), (False, 'native PAGE')])),
                ('Sample_Vial', models.CharField(max_length=120)),
                ('Amount_Of_Protein_Loaded', models.CharField(max_length=300)),
                ('Amount_Of_Protein_Loaded_Type', models.BooleanField(choices=[(True, 'loaded on gel'), (False, 'estimate about gel band')])),
                ('CUnit', models.CharField(choices=[(True, '\u03bcl'), (False, 'ml')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Specimen_PTM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Modification_Under_Investigation', models.CharField(max_length=120)),
                ('Species', models.CharField(max_length=120)),
                ('Taxon_id', models.CharField(max_length=120)),
                ('Sequence_Database_Public_Availability', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('Sequence_Database_Source', models.BooleanField()),
                ('Sequence_Database_File', models.FileField(upload_to=b'')),
                ('Sample_Type', models.CharField(choices=[('cell_pellet', 'cell pellet'), ('tissue', 'tissue'), ('protein_extract', 'protein extract')], max_length=50)),
                ('Sample_Vial', models.CharField(max_length=120)),
                ('Buffer_Composition', models.CharField(max_length=300)),
                ('Volume', models.FloatField()),
                ('VUnit', models.BooleanField(choices=[(True, '\u03bcl'), (False, 'ml')])),
                ('Protein_Concentration', models.FloatField()),
                ('CUnit', models.CharField(choices=[('nmol/ul', 'nmol/\u03bcl'), ('umol/ul', '\u03bcmol/\u03bcl'), ('mmol/ul', 'mmol/\u03bcl')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Specimen_SG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Species', models.CharField(max_length=120)),
                ('Taxon_id', models.CharField(max_length=120)),
                ('Sequence_Database_Public_Availability', models.BooleanField(choices=[(True, 'Yes'), (False, 'No')])),
                ('Sequence_Database_Source', models.CharField(max_length=50)),
                ('Sequence_Database_File', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/pportal/dev2/src/pportal/media'), upload_to=b'')),
                ('Sample_Type', models.CharField(choices=[('cell_pellet', 'cell pellet'), ('tissue', 'tissue'), ('protein_extract', 'protein extract')], max_length=50)),
                ('Sample_Vial', models.CharField(max_length=120)),
                ('Buffer_Composition', models.CharField(max_length=300)),
                ('Volume', models.FloatField()),
                ('VUnit', models.BooleanField(choices=[(True, '\u03bcl'), (False, 'ml')])),
                ('Protein_Concentration', models.FloatField()),
                ('CUnit', models.CharField(choices=[('nmol/ul', 'nmol/\u03bcl'), ('umol/ul', '\u03bcmol/\u03bcl'), ('mmol/ul', 'mmol/\u03bcl')], max_length=10)),
            ],
        ),
    ]