# Generated by Django 3.0.8 on 2020-07-07 02:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authenticator', '0002_auto_20200707_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_data',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
