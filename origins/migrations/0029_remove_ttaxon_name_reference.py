# Generated by Django 2.2.19 on 2021-05-03 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0028_ttaxon_name_reference'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ttaxon',
            name='name_reference',
        ),
    ]
