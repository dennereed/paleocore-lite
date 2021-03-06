# Generated by Django 2.2.5 on 2020-03-26 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eppe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taxon',
            name='label',
            field=models.CharField(blank=True, help_text='For a species, the name field contains the specific epithet and the label contains the full\n    scientific name, e.g. Homo sapiens, name = sapiens, label = Homo sapiens', max_length=244, null=True),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eppe.Taxon'),
        ),
        migrations.AlterField(
            model_name='taxon',
            name='rank',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eppe.TaxonRank'),
        ),
    ]
