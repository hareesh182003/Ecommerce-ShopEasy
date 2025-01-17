# Generated by Django 5.0.7 on 2024-12-07 04:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.RegexValidator('^[6-9]\\d{9}')]),
        ),
    ]
