# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-25 04:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('left', models.CharField(max_length=40)),
                ('right', models.CharField(max_length=40)),
                ('top', models.CharField(max_length=40)),
                ('bottom', models.CharField(max_length=40)),
                ('creator', models.CharField(max_length=20)),
                ('creation_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=6, null=True)),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('belong_plot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plotter.Plot')),
            ],
        ),
    ]
