from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import customer,car
from .forms import customerDe,carDe

 
# Create your views here.
def home(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def report(request):
    return render(request,'base_report.html')

def listing(request):
   return render(request,'base_listing.html')

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
def RTO(request):
    return render(request,'index_rto.html')

def insurance(request):
    return render(request,'index_insurance.html')

def other(request):
    return render(request,'index_other.html')

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

def formCar(request):
    if request.method == 'POST':
        fm = carDe(request.POST)
        if fm.is_valid():
            fm.save()
            fm = customerDe()

    else:
        fm = carDe()
    #data = customer.object.all()
    return render(request,'index_car.html',{'form':fm})

def DeleteDate(request,id):
    if request.method == 'POST' :
        pi = customer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/listing')


def UpdateData(request,id):
    print(id)
    if request.method =='POST':
        print("post")
        cus = customer.objects.get(pk=id)
        fm = customerDe(request.POST,instance=cus) 
        if fm.is_valid():
            fm.save()
        
        if car.objects.filter(CUS_ID=id).exists():
            car1 = car.objects.get(CUS_ID=id)
            cfm = carDe(request.POST,instance=car1) 
            if cfm.is_valid():
                cfm.save()
        else:
            cfm = carDe(request.POST)
            if cfm.is_valid():
                cfm.save()
        return HttpResponseRedirect('/listing/')
    
    else:
        print("else")
        cus = customer.objects.get(pk=id)
        fm = customerDe(instance=cus)
        car1 = car.objects.filter(CUS_ID=id).first()   
        fm2 = carDe(instance=car1,initial={'CUS_ID':id})
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

