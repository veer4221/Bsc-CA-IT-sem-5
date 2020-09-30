from django.db import models
# from datetime import datetime

# Create your models here.

class customer(models.Model):
    CUS_ID     = models.AutoField(primary_key=True)
    CUS_SARNAME = models.CharField(max_length=20,blank=True)
    CUS_NAME   = models.CharField(max_length=70,blank=True)
    CUS_FNAME   = models.CharField(max_length=70,blank=True)
    CUS_CITY   = models.CharField(max_length=70,blank=True)
    CUS_MO     = models.CharField(max_length=12,unique=True,blank=True)
    CUS_EMAIL  = models.EmailField(unique=True)
    CUS_STATE  = models.CharField(max_length=70)
    CUS_Zip    = models.CharField(max_length= 6)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.CUS_NAME

class car(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    CAR_ID     =models.AutoField(primary_key=True)
    CAR_MODEL  = models.CharField(max_length= 20,null=True)
    CAR_COLOUR = models.CharField(max_length= 20,null=True)
    CAR_COMPANY = models.CharField(max_length= 20,null=True)
    CAR_PRICE_OR = models.IntegerField(null=True)
    CAR_PRICE_EX = models.IntegerField(null=True)   
    CAR_BOOKING_AMT = models.IntegerField(null=True)
    CAR_BOOKING_DATE = models.DateField(null=True)
      
    
    def __str__(self):
        return self.CAR_MODEL

class insurance(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    INS_COMPANY_NAME = models.CharField(max_length= 20,blank=True)
    INS_TYPE         = models.CharField(max_length= 20,blank=True)
    INS_TOTAL_AMT    = models.IntegerField(blank=True)
    INS_TO_DATE      = models.DateField(blank=True)
    INS_FROM_DATE   = models.DateField(blank=True)


class RTO(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    RTO_REG_CHARGE  = models.IntegerField(blank=True)
    RTO_NUM_PLT_CHARGE = models.IntegerField(blank=True)
    RTO_NUM_PLT_NO   = models.CharField(max_length= 20,unique=True,blank=True)
    RTO_ENG_NO        = models.CharField(max_length= 20,unique=True,blank=True)
    RTO_CHESSISE_NO  = models.CharField(max_length= 20,unique=True,blank=True)
    RTO_KEY_NO       = models.CharField(max_length= 20,unique=True,blank=True)
    RTO_BATTERY_NO     = models.CharField(max_length= 20,unique=True,blank=True)
   
class OTHER(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    OTH_TRANS_CHARGE   = models.IntegerField(blank=True)
    OTH_DELIVERY_DATE   = models.DateField(blank=True)
    OTH_EXPENSE_NAME    = models.CharField(max_length= 20)
    OTH_EXPENSE_PRICE   = models.IntegerField(blank=True)
    date_modified = models.DateTimeField(auto_now=True)
   