# Generated by Django 3.1.1 on 2020-09-27 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0002_auto_20200927_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='CAR_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CUS_ID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
