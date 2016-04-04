# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 06:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_useraccess'),
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('active', models.BooleanField()),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('active', models.BooleanField()),
                ('date_created', models.DateTimeField(verbose_name='date created')),
            ],
        ),
        migrations.RemoveField(
            model_name='useraccess',
            name='user',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserAccess',
        ),
        migrations.AddField(
            model_name='computer',
            name='host_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.HostGroup'),
        ),
    ]