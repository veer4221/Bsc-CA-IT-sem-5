# Generated by Django 3.1.1 on 2020-09-30 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CAR', '0012_auto_20200930_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurance',
            name='INS_COMPANY_NAME',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_FROM_DATE',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_TOTAL_AMT',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_TO_DATE',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='insurance',
            name='INS_TYPE',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='other',
            name='OTH_DELIVERY_DATE',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='other',
            name='OTH_EXPENSE_PRICE',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='other',
            name='OTH_TRANS_CHARGE',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_BATTERY_NO',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_CHESSISE_NO',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_ENG_NO',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_KEY_NO',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_NUM_PLT_CHARGE',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_NUM_PLT_NO',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='rto',
            name='RTO_REG_CHARGE',
            field=models.IntegerField(null=True),
        ),
    ]
