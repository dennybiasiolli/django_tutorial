# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.SmallIntegerField(unique=True)),
                ('descrizione', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Ambiti',
            },
        ),
        migrations.CreateModel(
            name='Spesa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data_accredito', models.DateField()),
                ('data_riferimento', models.DateField()),
                ('importo', models.DecimalField(max_digits=15, decimal_places=2)),
                ('descrizione', models.CharField(max_length=300)),
                ('quantita', models.SmallIntegerField()),
                ('ambito', models.ForeignKey(to='budgest.Ambito')),
            ],
            options={
                'verbose_name_plural': 'Spese',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descrizione', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['descrizione'],
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.AddField(
            model_name='spesa',
            name='tags',
            field=models.ManyToManyField(to='budgest.Tag', blank=True),
        ),
    ]
