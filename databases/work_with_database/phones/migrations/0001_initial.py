# Generated by Django 2.2.6 on 2019-10-28 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.TextField()),
                ('releases_date', models.TextField()),
                ('lte_exists', models.BooleanField()),
                ('date', models.DateField()),
                ('slug', models.SlugField()),
            ],
        ),
    ]
