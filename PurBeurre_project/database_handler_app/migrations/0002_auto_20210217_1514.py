# Generated by Django 3.1.1 on 2021-02-17 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database_handler_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myusers',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
