# Generated by Django 2.2.19 on 2021-05-04 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('origins', '0035_auto_20210504_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ttaxon',
            name='classification_status',
            field=models.CharField(blank=True, choices=[('accepted', 'Accepted'), ('junior_synonym', 'Junior Synonym'), ('deprecated', 'Deprecated')], default='ICZN', max_length=255, null=True, verbose_name='Classif. Status'),
        ),
        migrations.AlterField(
            model_name='ttaxon',
            name='nomenclatural_status',
            field=models.CharField(blank=True, choices=[('valid', 'Valid'), ('invalid_gh', 'Invalid GH'), ('invalid_ga', 'Invalid GA'), ('invalid_gb', 'Invalid GB'), ('invalid_sh', 'Inavlid SH'), ('invalid_sm', 'Invalid SM'), ('invalid_sn', 'Invalid SN'), ('invalid_so', 'Inavlid SO'), ('suppressed', 'Supressed')], max_length=255, null=True, verbose_name='Nom. Status'),
        ),
    ]