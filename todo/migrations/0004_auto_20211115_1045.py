# Generated by Django 3.2.9 on 2021-11-15 08:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_rename_task_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(3)])),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
        migrations.AddField(
            model_name='todo',
            name='tags',
            field=models.ManyToManyField(to='todo.Tag'),
        ),
    ]
