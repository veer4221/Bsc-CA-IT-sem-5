from django.shortcuts import render,HttpResponseRedirect,HttpResponse,redirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import customer,car,insurance,RTO,OTHER,IMG
from .forms import customerDe,carDe,insuranceDe,RTODE,OTHERDE,reportDE
from easy_pdf.views import PDFTemplateView,PDFTemplateResponseMixin
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.db.models import Sum 
from django.contrib.staticfiles import finders
import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# from django.http import HttpResponse
from django.conf import settings
from datetime import date 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.db.models import Count,Q
from collections import Counter 
# Create your views here.
#def home(request):
 #   return render(request,'index.html')

#def base(request):
 #   return render(request,'base.html')

def report(request):

   
    if request.method == 'POST':
     
    
        to = request.POST.get('to_date')
        frome = request.POST.get('from_date')
        
        cus_id1 = OTHER.objects.filter(Q(OTH_DELIVERY_DATE__gte=to) & Q(OTH_DELIVERY_DATE__lte=frome)).values('CUS_ID')
        CUS_TBL = customer.objects.filter(CUS_ID__in=cus_id1)
        INS_TBL = insurance.objects.filter(CUS_ID__in=cus_id1)
        CAR_TBL = car.objects.filter(CUS_ID__in=cus_id1)
        RTO_TBL = RTO.objects.filter(CUS_ID__in=cus_id1)
        OTH_TBL = OTHER.objects.filter(CUS_ID__in=cus_id1)
        print(CUS_TBL)
        mylist = zip(CUS_TBL,CAR_TBL,INS_TBL,RTO_TBL,OTH_TBL)
        return render(request,'report.html',{'cus':CUS_TBL,'car':CAR_TBL,'ins':INS_TBL,'rto':RTO_TBL,'other':OTH_TBL,'mylist':mylist})
    else:
        fm = reportDE()
        # print(cos)
        return render(request,'report.html',{'form':fm})
    

# def listing(request):
#    return render(request,'base_listing.html')

def dashbord(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')

    all_data_cus = customer.objects.all()
    Count_cus = all_data_cus.aggregate(Count('CUS_ID'))
    all_data_other = OTHER.objects.all()
    Count_OTH = all_data_other.aggregate(Count('OTH_ID'))
    # print(Count_OTH)
    # temp1 = Counter(Count_cus) 
    # temp2 = Counter(Count_OTH)
    t1  = list(Count_cus.values())
    t2  = list(Count_OTH.values())
    t3  = int(t1[0]-t2[0])
    

    # print(active)
    # {key: Count_cus[] - Count_OTH[]}  


    context={'Con':Count_cus,'Other':Count_OTH,'active':t3}
    return render(request,'main_dash.html',context)


def login(request):

    if request.method == 'POST':
        print('post')
        fm= AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            print(uname)
            upass = fm.cleaned_data['password']
            print(upass)

            user = authenticate(username=uname,password=upass)
            if user is not None:
                print('valid1')
                auth_login(request,user)
                print('valid2')
                return HttpResponseRedirect('/dashbord/')
    else:
        fm= AuthenticationForm()

        print('get re')
    return render(request,'login.html',{'form':fm})

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

# def car(request):
#     return render(request,'index_car.html')

# def customer(request):
#     if request.method == 'POST':
#         fm = customerDe(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = customerDe()

#     else:
#         fm = customerDe()
#     #data = customer.object.all()
#     return render(request,'index_customer.html',{'form':fm})
a = 2
#def RTO(request):
 #   return render(request,'index_rto.html')

# def insurance(request):
    # return render(request,'index_insurance.html')

# def other(request):
    # return render(request,'index_other.html')

class customerView(LoginRequiredMixin,ListView):
    model = customer
    login_url = '/login/'
    template_name ='base_listing.html'

class formToDB(LoginRequiredMixin,TemplateView):
    template_name = 'index_customer.html'
    login_url = '/login/'
    def get_context_data(self, *arg, **kwargs):
        fm = customerDe()
        context = {'form':fm}
        return context
    
    def post(self,request,id=0):     
        fm = customerDe(request.POST)
        if fm.is_valid():
            fm.save()
            print(fm)
            return HttpResponseRedirect('/listing')   

# class formCartoDB(TemplateView):
#     template_name = 'index_car.html'
#     def get_context_data(self, *arg, **kwargs):
#         fm = formCartoDB()
#         context = {'form2':fm}
#         return context
    
#     def post(self,request,id=0):
#         fm = carDe(request.POST)
#         if fm.is_valid():
#             fm.save()
#             print(fm)
#             return HttpResponseRedirect('/listing')   

# def formCar(request):
#     if request.method == 'POST':
#         fm = carDe(request.POST)
#         if fm.is_valid():
#             fm.save()
#             fm = customerDe()

#     else:
#         fm = carDe()
#     #data = customer.object.all()
#     return render(request,'index_car.html',{'form':fm})

def DeleteDate(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST' :
            pi = customer.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/listing')
    else:
        return HttpResponseRedirect('/login/')

def UpdateData(request,id):
    print(id)
    if request.user.is_authenticated:
        if request.method =='POST':
            print(request)
    ############### Custmer Update ############## 
            cus = customer.objects.get(pk=id)
            fm = customerDe(request.POST,instance=cus) 
            if fm.is_valid():
                fm.save()
    ############## car Update ############## 
            if car.objects.filter(CUS_ID=id).exists():
                car1 = car.objects.get(CUS_ID=id)
                fm2 = carDe(request.POST,instance=car1) 
                if fm2.is_valid():
                    fm2.save()
            else:
                cfm = carDe(request.POST)
                if cfm.is_valid():
                    cfm.save()
    ############### INS Update ##############  
            if insurance.objects.filter(CUS_ID=id).exists():
                ins = insurance.objects.get(CUS_ID=id)
                fm3 = insuranceDe(request.POST,instance=ins) 
                if fm3.is_valid():
                    fm3.save()
                    print(fm3)
            else:
                cfm3 = insuranceDe(request.POST)
                if cfm3.is_valid():
                    cfm3.save()
    ############## RTO #######################
            if RTO.objects.filter(CUS_ID=id).exists():
                rt = RTO.objects.get(CUS_ID=id)
                fm4 = RTODE(request.POST,instance=rt) 
                if fm4.is_valid():
                    fm4.save()
                    print(fm4)
            else:
                fm4 = RTODE(request.POST)
                if fm4.is_valid():
                    fm4.save()

        
    ############ OTHER  #####################
            if OTHER.objects.filter(CUS_ID=id).exists():
                ot = OTHER.objects.get(CUS_ID=id)
                fm5 = OTHERDE(request.POST,instance=ot) 
                if fm5.is_valid():
                    fm5.save()
                    print(fm5)
            else:
                cfm3 = OTHERDE(request.POST)
                if cfm3.is_valid():
                    cfm3.save()
            
            
            return HttpResponseRedirect('/%s/'%id)
        #/classroom/notamember/%s/' % classname)
        else:
    ########### customerForm ###############
            print("else")
            cus = customer.objects.get(pk=id)
            fm = customerDe(instance=cus)
    #############car form #################
            car1 = car.objects.filter(CUS_ID=id).first()
            print('car1',car1)   
            fm2 = carDe(instance=car1,initial={'CUS_ID':id})
    ############## ins form ######################
            ins = insurance.objects.filter(CUS_ID=id).first()
            print('ins',ins)   
            fm3 = insuranceDe(instance=ins,initial={'CUS_ID':id})
    ############### RTO #####################
            rt = RTO.objects.filter(CUS_ID=id).first()
            print('ins',rt)   
            fm4 = RTODE(instance=rt,initial={'CUS_ID':id})
    ############## OTHER #####################
            ot = OTHER.objects.filter(CUS_ID=id).first()
            print('ins',ot)   
            fm5 = OTHERDE(instance=ot,initial={'CUS_ID':id})
            if car.objects.filter(CUS_ID=id).exists():
                return render(request,'index_customerUpdate.html',{'form':fm,'form2':fm2,'form3':fm3,'form4':fm4,'form5':fm5,'id':id})
            else:
                return render(request,'index_customerUpdate.html',{'form':fm,'form2':fm2,'id':id})
    else:
        return HttpResponseRedirect('/login/')
    #     else:
    #         cr = car.objects.get(pk=id)
    #         cfm = carDe(instance=cr)
    # if car.objects.filter(pk=id).exists():
    #     return render(request,'index_customerUpdate.html',{'form':fm,'form2':cfm})
    # else:
    #     return render(request,'index_customerUpdate.html',{'form':fm})


        
    
# def car(request,id=0):
#     if request.method =='POST':
#         pi = customer.objects.get(pk=a)
#         fm = customerDe(request.POST,instance=pi)
#         if fm.is_valid():
#             fm.save()
#     else:        
#         pi = customer.objects.get(pk=a)
#         fm = customerDe(instance=pi)
    
#     return render(request,'index_car.html',{'form':fm})

# def temp(request):
#     st = insurance.objects.all()
#     return render(request,'index_rto.html',{'st':st})


# def export_pdf(request,id):
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'inline; attachment; filename=Expances' + \
#         str(datetime.datetime.now())+'.pdf'
#     response['Content-Transfer-Encoding'] ='binary'
#     c = car.objects.get(CUS_ID=id)
    
#     html_string = render_to_string('pdf_des.html',{'expance':c,})
#     html = HTML(string=html_string)

#     result = html.write_pdf() 

#     with tempfile.NamedTemporaryFile(delete=True) as output:
#         output.write(result)
#         output.flush()

#         output=open(output.name,'rb')
#         response.write(output.read())

#     return response   

def render_pdf_view(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    id = kwargs.get('id')
    cus = customer.objects.get(CUS_ID=id) 
    c = car.objects.get(CUS_ID=id) 
    IN = insurance.objects.get(CUS_ID=id) 
    RT = RTO.objects.get(CUS_ID=id) 
    OT = OTHER.objects.get(CUS_ID=id) 
    im = IMG.objects.get(id=1)
    cp = car.objects.only('CAR_PRICE_EX').get(CUS_ID=id).CAR_PRICE_EX
    RTOC = RTO.objects.only('RTO_REG_CHARGE').get(CUS_ID=id).RTO_REG_CHARGE
    tpc =OTHER.objects.only('OTH_TRANS_CHARGE').get(CUS_ID=id).OTH_TRANS_CHARGE
    npc= RTO.objects.only('RTO_NUM_PLT_CHARGE').get(CUS_ID=id).RTO_NUM_PLT_CHARGE
    oex =OTHER.objects.only('OTH_EXPENSE_PRICE').get(CUS_ID=id).OTH_EXPENSE_PRICE
    insA=insurance.objects.only('INS_TOTAL_AMT').get(CUS_ID=id).INS_TOTAL_AMT
    add = cp+RTOC+tpc+npc+oex+insA
    print(add)
    print(RTOC)
    namw =customer.objects.only('CUS_NAME').get(CUS_ID=id).CUS_NAME
    print(im)
    print("hello")
    bill_date = date.today()
    print(cus)
    template_path = 'pdf_des.html'
    context = {'customer': cus,'car':c,'im':im,'bill_date':bill_date,'ins':IN,'RTO':RT,'other':OT,'totel':add}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename=invoice' + namw +str(datetime.datetime.now())+'.pdf'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def AddCarModel(request):
    
    return render(request,'add_carmodal.html')