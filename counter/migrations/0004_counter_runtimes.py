# Generated by Django 2.2.4 on 2019-08-27 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0003_auto_20190826_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='counter',
            name='runtimes',
            field=models.IntegerField(default=0),
        ),
    ]
