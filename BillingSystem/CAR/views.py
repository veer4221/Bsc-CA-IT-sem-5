from django.shortcuts import render,HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import customer,car
from .forms import customerDe

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

def car(request):
    return render(request,'index_car.html')

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
            return HttpResponseRedirect('/listing')   



def DeleteDate(request,id):
    if request.method == 'POST' :
        pi = customer.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/listing')


def UpdateData(request,id):
    if request.method =='POST':
        pi = customer.objects.get(pk=id)
        fm = customerDe(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = customer.objects.get(pk=id)
        fm = customerDe(instance=pi)
    return render(request,'index_customerUpdate.html',{'form':fm})


        
    
    