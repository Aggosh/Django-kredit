# Generated by Django 2.2.6 on 2019-10-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0017_notification_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='company_name',
            field=models.CharField(choices=[('Dinero', '//Dinero//'), ('Moneyveo', 'https://www.google.com/'), ('Credit7', 'https://targetme.go2cloud.org/SHk'), ('MyCredit', 'https://www.google.com/'), ('Miloan', 'https://www.google.com/'), ('Kredit-Plus', 'https://www.google.com/'), ('AlexCredit', 'https://www.google.com/'), ('BystroZajm', 'https://www.google.com/')], default='-', max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='company_name',
            field=models.CharField(choices=[('//Dinero//', 'Dinero'), ('https://www.google.com/', 'Moneyveo'), ('https://targetme.go2cloud.org/SHk', 'Credit7'), ('https://www.google.com/', 'MyCredit'), ('https://www.google.com/', 'Miloan'), ('https://www.google.com/', 'Kredit-Plus'), ('https://www.google.com/', 'AlexCredit'), ('https://www.google.com/', 'BystroZajm')], default='-', max_length=255),
        ),
    ]
