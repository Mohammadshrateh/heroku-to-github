# Generated by Django 3.2.9 on 2021-11-15 06:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]