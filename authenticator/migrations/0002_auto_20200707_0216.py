# Generated by Django 3.0.8 on 2020-07-07 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_data',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]