# Generated by Django 3.2.5 on 2021-08-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_samplemodel_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplemodel',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]