from django.core import validators
from django import forms
from .models import car,customer
#from bootstrap_modal_forms.forms import BSModalModelForm



class customerDe(forms.ModelForm):
    class Meta:
        model = customer
        fields =['CUS_ID','CUS_SARNAME','CUS_NAME','CUS_FNAME','CUS_CITY','CUS_MO','CUS_EMAIL','CUS_STATE','CUS_Zip']
        widgets={
            'CUS_ID' : forms.TextInput(attrs={'class':'sr-only'}),
            'CUS_SARNAME': forms.TextInput(attrs={'class':'form-control'}),
            'CUS_NAME': forms.TextInput(attrs={'class':'form-control'}),
            'CUS_FNAME' : forms.TextInput(attrs={'class':'form-control'}),
            'CUS_CITY': forms.TextInput(attrs={'class':'form-control'}),
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
            'CAR_BOOKING_DATE': forms.DateInput(attrs={'class':'form-control'}),
            
        }
