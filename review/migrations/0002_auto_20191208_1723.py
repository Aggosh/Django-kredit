# Generated by Django 2.2.7 on 2019-12-08 15:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='company_nama',
            new_name='company_name',
        ),
    ]
