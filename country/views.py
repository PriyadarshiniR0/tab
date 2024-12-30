from django.shortcuts import render
from django.http import HttpResponse
from country.models import *

# Create your views here.
def insert_co(request):
    no=int(input('Enter the country no:'))
    name=input('Enter the country name:')
    CTO=Country.objects.get_or_create(cno=no,cname=name)
    if CTO[1]:
         CTO=Country.objects.all()
         d={'CTO':CTO}
         return render(request,'display_country.html',d)
    else:
        return HttpResponse('Country is not created!!')
    
    
def insert_ca(request):
    cna=input('Enter the capital name:')
    cno=int(input('Enter the capital no :'))
    c_name=input('Enter the Country name:')
    c_nameobj=Country.objects.get(cname=c_name)
    CATO=Capital.objects.get_or_create(capname=cna,capno=cno,cname=c_nameobj)
    if CATO[0]:
        CATO=Capital.objects.all()
        d={'CATO':CATO}
        return render(request,'display_capital.html',d)
    else:
        return HttpResponse('With the given details, the Countrys capital is exisiting')
    
def display_country(request):
    CTO=Country.objects.all()
    d={'CTO':CTO}
    return render(request,'display_country.html',d)

def display_capital(request):
    CATO=Capital.objects.all()
    d={'CATO':CATO}
    return render(request,'display_capital.html',d) 

    


    
