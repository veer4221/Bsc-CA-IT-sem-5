from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import customer,car,insurance,RTO,OTHER
from .forms import customerDe,carDe,insuranceDe,RTODE,OTHERDE

 
# Create your views here.
#def home(request):
 #   return render(request,'index.html')

#def base(request):
 #   return render(request,'base.html')

# def report(request):
#     return render(request,'base_report.html')

# def listing(request):
#    return render(request,'base_listing.html')

def dashbord(request):
    return render(request,'base_dashbord.html')

def login(request):
    return render(request,'login.html')

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

class customerView(ListView):
    model = customer
    template_name ='base_listing.html'

class formToDB(TemplateView):
    template_name = 'index_customer.html'
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
    if request.method == 'POST' :
        pi = customer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/listing')


def UpdateData(request,id):
    print(id)
    if request.method =='POST':
        print(request)
       ############### Custmer Update ############## 
        cus = customer.objects.get(pk=id)
        fm = customerDe(request.POST,instance=cus) 
        if fm.is_valid():
            fm.save()
       ############### car Update ############## 
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
        
        
        return HttpResponseRedirect('/listing')
    
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
        ############### OTHER #####################
        ot = OTHER.objects.filter(CUS_ID=id).first()
        print('ins',ot)   
        fm5 = OTHERDE(instance=ot,initial={'CUS_ID':id})
        if car.objects.filter(CUS_ID=id).exists():
            return render(request,'index_customerUpdate.html',{'form':fm,'form2':fm2,'form3':fm3,'form4':fm4,'form5':fm5})
        else:
            return render(request,'index_customerUpdate.html',{'form':fm,'form2':fm2})
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