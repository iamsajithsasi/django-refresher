# Generated by Django 3.2.5 on 2021-08-09 17:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_samplemodel_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='samplemodel',
            name='details',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
