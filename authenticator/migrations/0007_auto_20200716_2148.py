# Generated by Django 3.0.8 on 2020-07-16 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0006_auto_20200716_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_data',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='personal_data',
            name='weigth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]