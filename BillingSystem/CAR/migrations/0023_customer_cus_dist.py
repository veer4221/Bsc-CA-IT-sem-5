# Generated by Django 3.1.1 on 2020-10-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0022_auto_20201005_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='CUS_DIST',
            field=models.CharField(default='NULL', max_length=30),
        ),
    ]
