# Generated by Django 2.1.1 on 2019-10-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phone',
            name='date',
        ),
        migrations.AlterField(
            model_name='phone',
            name='releases_date',
            field=models.DateField(),
        ),
    ]
