from django.core import validators
from django import forms
from .models import car,customer,insurance,RTO,OTHER
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#from bootstrap_modal_forms.forms import BSModalModelForm

class DateInput(forms.DateInput):
    input_type='date'

class customerDe(forms.ModelForm):
    class Meta:
        model = customer
        fields =['CUS_ID','CUS_SARNAME','CUS_NAME','CUS_FNAME','CUS_CITY','CUS_TALUKA','CUS_DIST','CUS_MO','CUS_EMAIL','CUS_STATE','CUS_Zip']
        widgets={
            'CUS_ID' : forms.TextInput(attrs={'class':'form-inline'}),
            'CUS_SARNAME': forms.TextInput(attrs={'class':'form-control'}),
            'CUS_NAME': forms.TextInput(attrs={'class':'form-control'}),
            'CUS_FNAME' : forms.TextInput(attrs={'class':'form-control'}),
            'CUS_CITY': forms.TextInput(attrs={'class':'form-control'}),
            'CUS_TALUKA':forms.TextInput(attrs={'class':'form-control'}),
            'CUS_DIST' :forms.TextInput(attrs={'class':'form-control'}),
            'CUS_MO':forms.TextInput(attrs={'class':'form-control'}),
            'CUS_EMAIL': forms.EmailInput(attrs={'class':'form-control'}),
            'CUS_STATE': forms.TextInput(attrs={'class':'form-control'}),
            'CUS_Zip': forms.TextInput(attrs={'class':'form-control'}),
            

        }

  
class carDe(forms.ModelForm):
    class Meta:
        model = car
        fields =['CUS_ID','CAR_ID','CAR_MODEL','CAR_COLOUR','CAR_COMPANY','CAR_PRICE_OR','CAR_PRICE_EX','CAR_BOOKING_AMT','CAR_BOOKING_DATE']
        widgets={
            'CUS_ID':forms.NumberInput(attrs={'class':'form-control'}),
            'CAR_ID' : forms.TextInput(attrs={'class':'sr-only'}),
            'CAR_MODEL': forms.TextInput(attrs={'class':'form-control'}),
            'CAR_COLOUR': forms.TextInput(attrs={'class':'form-control'}),
            'CAR_COMPANY' : forms.TextInput(attrs={'class':'form-control'}),
            'CAR_PRICE_OR': forms.NumberInput(attrs={'class':'form-control'}),
            'CAR_PRICE_EX':forms.NumberInput(attrs={'class':'form-control'}),
            'CAR_BOOKING_AMT': forms.NumberInput(attrs={'class':'form-control'}),
            'CAR_BOOKING_DATE':DateInput(attrs={'class':'form-control'}),
            
        }

class insuranceDe(forms.ModelForm):
    class Meta:
        model = insurance
        fields =['CUS_ID','INS_COMPANY_NAME','INS_TYPE','INS_TOTAL_AMT','INS_TO_DATE','INS_FROM_DATE']
        widgets={
        'CUS_ID':forms.NumberInput(attrs={'class':'form-control'}),
        'INS_COMPANY_NAME': forms.TextInput(attrs={'class':'form-control'}),
        'INS_TYPE': forms.TextInput(attrs={'class':'form-control'}),
        'INS_TOTAL_AMT':forms.NumberInput(attrs={'class':'form-control'}),
        'INS_TO_DATE': DateInput(attrs={'class':'form-control'}),
        'INS_FROM_DATE': DateInput(attrs={'class':'form-control'}),
        }

class RTODE(forms.ModelForm):
    class Meta:
        model = RTO
        fields =['CUS_ID','RTO_ID','RTO_REG_CHARGE','RTO_NUM_PLT_CHARGE','RTO_NUM_PLT_NO','RTO_ENG_NO','RTO_CHESSISE_NO']
        widgets={
        'CUS_ID':forms.NumberInput(attrs={'class':'form-control'}),
        'RTO_ID':forms.NumberInput(attrs={'class':'form-control'}),
        'RTO_REG_CHARGE':forms.NumberInput(attrs={'class':'form-control'}),
        'RTO_NUM_PLT_CHARGE':forms.NumberInput(attrs={'class':'form-control'}),
        'RTO_NUM_PLT_NO':forms.TextInput(attrs={'class':'form-control'}),
        'RTO_ENG_NO':forms.TextInput(attrs={'class':'form-control'}),
        'RTO_CHESSISE_NO':forms.TextInput(attrs={'class':'form-control'}),
        # 'RTO_KEY_NO':forms.TextInput(attrs={'class':'form-control'}),
        # 'RTO_BATTERY_NO':forms.TextInput(attrs={'class':'form-control'}),

        }

class OTHERDE(forms.ModelForm):
    class Meta:
        model = OTHER
        fields =['CUS_ID','OTH_ID','OTH_TRANS_CHARGE', 'OTH_DELIVERY_DATE', 'OTH_EXPENSE_NAME', 'OTH_EXPENSE_PRICE']
        widgets={
        'CUS_ID' :forms.NumberInput(attrs={'class':'form-control'}),
        'OTH_ID' :forms.NumberInput(attrs={'class':'form-control'}),
        'OTH_TRANS_CHARGE' :forms.NumberInput(attrs={'class':'form-control'}),
        'OTH_DELIVERY_DATE': DateInput(attrs={'class':'form-control'}),
        'OTH_EXPENSE_NAME' : forms.TextInput(attrs={'class':'form-control'}),
        'OTH_EXPENSE_PRICE' :forms.NumberInput(attrs={'class':'form-control'}),
        }


# class ADDCAR(forms.ModelForm):
#     class Meta:
#         model = AadCar
#         fields =['CAR_MODEL']
#         widgets={
#             'OTH_EXPENSE_NAME' : forms.TextInput(attrs={'class':'form-control'})
#             }