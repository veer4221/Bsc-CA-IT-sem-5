# Generated by Django 3.1.1 on 2020-09-30 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0011_auto_20200930_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insurance',
            name='id',
        ),
        migrations.RemoveField(
            model_name='other',
            name='id',
        ),
        migrations.RemoveField(
            model_name='rto',
            name='id',
        ),
        migrations.AddField(
            model_name='insurance',
            name='INS_ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='other',
            name='OTH_ID',
            field=models.AutoField(default=2, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rto',
            name='RTO_ID',
            field=models.AutoField(default=12, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='CUS_CITY',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CUS_FNAME',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CUS_MO',
            field=models.CharField(blank=True, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CUS_NAME',
            field=models.CharField(blank=True, max_length=70),
        ),
        migrations.AlterField(
            model_name='customer',
            name='CUS_SARNAME',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_COMPANY_NAME',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_FROM_DATE',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_TOTAL_AMT',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_TO_DATE',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_TYPE',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='other',
            name='OTH_DELIVERY_DATE',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='other',
            name='OTH_EXPENSE_PRICE',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='other',
            name='OTH_TRANS_CHARGE',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_BATTERY_NO',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_CHESSISE_NO',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_ENG_NO',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_KEY_NO',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_NUM_PLT_CHARGE',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_NUM_PLT_NO',
            field=models.CharField(blank=True, max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_REG_CHARGE',
            field=models.IntegerField(blank=True),
        ),
    ]
