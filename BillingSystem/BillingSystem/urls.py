"""BillingSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from CAR import views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
 #   path('listing/form/',views.home,name="home"),
 #   path('base/',views.base,name="base"),
 #   path('report/',views.report,name="report"),
    path('listing/',views.customerView.as_view(),name="listing"),
    path('dashbord/',views.dashbord,name="dashbord"),
    # path('listing/Car/',views.car,name="car"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('listing/Costomer/',views.formToDB.as_view(),name="Costomer"),
#    path('listing/Car/',views.formCar,name="Car"),
    # path('listing/RTO/',views.temp,name="RTO"),
    # path('listing/other/',views.other,name="other"),
   # path('listing/Insurance/',views.insurance,name="Insurance"),
    path('Delete/<int:id>/',views.DeleteDate,name="Delete"),     
    path('<int:id>/',views.UpdateData,name="Update"),        
   # path('export-pdf/<id>/',views.export_pdf,name="pdf")
    path('export-pdf/<int:id>/',views.render_pdf_view,name="pdf"),
    path('add-car/',views.AddCarModel,name="addcar"),

]



# CAR_car.CUS_ID_id



