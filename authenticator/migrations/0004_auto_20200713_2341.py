# Generated by Django 3.0.8 on 2020-07-13 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0003_personal_data_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_data',
            name='birth_date',
            field=models.DateField(blank=True, verbose_name='%Y-%m-%d'),
        ),
    ]