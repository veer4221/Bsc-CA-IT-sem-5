from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime,date

# from datetime import datetime

# Create your models here.


class customer(models.Model):
    CUS_ID     = models.AutoField(primary_key=True)
    CUS_SARNAME = models.CharField(max_length=20,blank=True)
    CUS_NAME   = models.CharField(max_length=70,blank=True)
    CUS_FNAME   = models.CharField(max_length=70,blank=True)
    CUS_CITY   = models.CharField(max_length=70,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,10}$', message="Enter 10 digits ")
    CUS_MO     = models.CharField(validators=[phone_regex],max_length=15,unique=True,blank=True)
    CUS_EMAIL  = models.EmailField(unique=True)
    CUS_STATE  = models.CharField(max_length=70)
    zip_regex= RegexValidator(regex='\d[0-9]')
    CUS_Zip    = models.CharField(validators=[zip_regex],max_length= 6)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.CUS_NAME

class car(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    CAR_ID     =models.AutoField(primary_key=True)
    CAR_MODEL  = models.CharField(max_length=45)
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
    INS_ID     =models.AutoField(primary_key=True)
    INS_COMPANY_NAME = models.CharField(max_length= 20,null=True)
    INS_TYPE         = models.CharField(max_length= 20,null=True)
    INS_TOTAL_AMT    = models.IntegerField(null=True)
    INS_TO_DATE      = models.DateField(null=True)
    INS_FROM_DATE   = models.DateField(null=True)
    
    def __str__(self):
        return self.INS_COMPANY_NAME



class RTO(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    RTO_ID     =models.AutoField(primary_key=True)
    RTO_REG_CHARGE  = models.IntegerField(null=True)
    RTO_NUM_PLT_CHARGE = models.IntegerField(null=True)
    CHESSISE_regex = RegexValidator(regex=r'[A-Z0-9]{16,17}$',)
    RTO_NUM_PLT_NO   = models.CharField(max_length= 20,unique=True,null=True)
    RTO_ENG_NO        = models.CharField(validators=[CHESSISE_regex],max_length= 17,unique=True,null=True)
    RTO_CHESSISE_NO  = models.CharField(validators=[CHESSISE_regex],max_length= 17,unique=True,null=True)
    RTO_KEY_NO       = models.CharField(validators=[CHESSISE_regex],max_length= 17,unique=True,null=True)
    RTO_BATTERY_NO     = models.CharField(max_length= 20,unique=True,null=True)
   
class OTHER(models.Model):
    CUS_ID     = models.ForeignKey(customer,on_delete=models.CASCADE)
    OTH_ID     =models.AutoField(primary_key=True)
    OTH_TRANS_CHARGE   = models.IntegerField(null=True)
    OTH_DELIVERY_DATE   = models.DateField(null=True)
    OTH_EXPENSE_NAME    = models.CharField(max_length= 20)
    OTH_EXPENSE_PRICE   = models.IntegerField(null=True)
    date_modified = models.DateTimeField(auto_now=True)


class IMG(models.Model):
    IMG = models.ImageField()



   