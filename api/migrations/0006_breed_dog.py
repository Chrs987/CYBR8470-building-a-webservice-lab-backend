# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-16 19:09
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170905_2054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('size', models.CharField(choices=[('tiny', 'Tiny'), ('small', 'Small'), ('medium', 'Medium'), ('large', 'Large')], default='tiny', max_length=10)),
                ('friendliness', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('trainability', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('sheddingAmount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('exerciseNeeds', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=7)),
                ('color', models.CharField(max_length=10)),
                ('favoriteFood', models.CharField(max_length=10)),
                ('favoriteToy', models.CharField(max_length=20)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Breed')),
            ],
        ),
    ]
