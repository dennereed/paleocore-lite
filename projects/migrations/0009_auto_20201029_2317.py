# Generated by Django 2.2.13 on 2020-10-29 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_auto_20200807_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectpage',
            name='app_label',
            field=models.CharField(blank=True, choices=[('compressor', 'compressor'), ('joyous', 'joyous'), ('publications', 'publications'), ('projects', 'projects'), ('standard', 'standard'), ('drp', 'drp'), ('mlp', 'mlp'), ('hrp', 'hrp'), ('lgrp', 'lgrp'), ('eppe', 'eppe'), ('gdb', 'gdb'), ('omo_mursi', 'omo_mursi'), ('origins', 'origins'), ('psr', 'psr'), ('cc', 'cc'), ('fc', 'fc'), ('wtap', 'wtap'), ('eval', 'eval')], max_length=100, null=True),
        ),
    ]
