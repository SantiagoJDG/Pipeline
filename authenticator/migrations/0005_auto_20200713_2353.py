# Generated by Django 3.0.8 on 2020-07-13 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0004_auto_20200713_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_data',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
    ]
