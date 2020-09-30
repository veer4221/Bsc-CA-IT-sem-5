from django.db import models
# from datetime import datetime

# Create your models here.

class customer(models.Model):
    CUS_ID     = models.AutoField(primary_key=True)
    CUS_SARNAME = models.CharField(max_length=20,null=False)
    CUS_NAME   = models.CharField(max_length=70,null=False)
    CUS_FNAME   = models.CharField(max_length=70,null=False)
    CUS_CITY   = models.CharField(max_length=70,null=False)
    CUS_MO     = models.CharField(max_length=12,unique=True,null=False)
    CUS_EMAIL  = models.EmailField(unique=True)
    CUS_STATE  = models.CharField(max_length=70)
    CUS_Zip    = models.CharField(max_length= 6)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.CUS_NAME

class car(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    CAR_ID     =models.AutoField(primary_key=True)
    CAR_MODEL  = models.CharField(max_length= 20,null=False)
    CAR_COLOUR = models.CharField(max_length= 20,null=False)
    CAR_COMPANY = models.CharField(max_length= 20,null=False)
    CAR_PRICE_OR = models.IntegerField()
    CAR_PRICE_EX = models.IntegerField()   
    CAR_BOOKING_AMT = models.IntegerField()
    CAR_BOOKING_DATE = models.DateField()
      
    
    def __str__(self):
        return self.CAR_MODEL

class insurance(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    INS_COMPANY_NAME = models.CharField(max_length= 20)
    INS_TYPE         = models.CharField(max_length= 20)
    INS_TOTAL_AMT    = models.IntegerField()
    INS_TO_DATE      = models.DateField()
    INS_FROM_DATE   = models.DateField()


class RTO(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    RTO_REG_CHARGE  = models.IntegerField()
    RTO_NUM_PLT_CHARGE = models.IntegerField()
    RTO_NUM_PLT_NO   = models.CharField(max_length= 20,unique=True)
    RTO_ENG_NO        = models.CharField(max_length= 20,unique=True)
    RTO_CHESSISE_NO  = models.CharField(max_length= 20,unique=True)
    RTO_KEY_NO       = models.CharField(max_length= 20,unique=True)
    RTO_BATTERY_NO     = models.CharField(max_length= 20,unique=True)
   
class OTHER(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    OTH_TRANS_CHARGE   = models.IntegerField()
    OTH_DELIVERY_DATE   = models.DateField()
    OTH_EXPENSE_NAME    = models.CharField(max_length= 20)
    OTH_EXPENSE_PRICE   = models.IntegerField()
    date_modified = models.DateTimeField(auto_now=True)
   