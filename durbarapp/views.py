from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.http import HttpResponse
from .import models
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.db.models import Sum
from .import models
import datetime
from django.core import serializers
import json
from django.http import JsonResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string, os
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.decorators import login_required
import hashlib, socket


def homepage(request):
    
    return render (request, 'durbarapp/index.html')

def merchant_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = models.MerchantInfo.objects.filter(email = email,password = password).first()
        
        if user is None:
            messages.warning(request, "Wrong Information")
            return render(request,'durbarapp/merchant_login.html')
        request.session['id'] = user.id
        return redirect('/merchant-dashboard/')  
    return render (request, 'durbarapp/merchant_login.html')

def merchant_dashboard(request): 
    if request.session['id'] == False:
        return redirect('merchant-login')
     

    return render (request, 'merchant_dashboard/index.html')

def merchant_register(request):
    district_list = models.DistrictEntry.objects.filter(status = True) 
    for data in district_list:
        print(data.id)
    context ={
        'district_list':district_list,
    }
    return render (request, 'durbarapp/register.html', context)

def merchant_dashboard(request): 
    if request.session['id'] == False:
        return redirect('merchant-login')
     

    return render (request, 'merchant_dashboard/index.html')

 
def merchant_logout(request):
    request.session['id'] = False
    return redirect('/')


 

def bind_upozilla(request):
    print("Test 111")
    district_id   = request.GET.get('district_id')
      
    district_wise_upozilla = models.UpozillaEntry.objects.filter(district_name_id = district_id)
    context = {
        'district_wise_upozilla': district_wise_upozilla,
    }
    return render(request, 'durbarapp/bind_district_wise_upo.html', context)

# def bind_upozilla_wise_postoffice(request):
#     upozilla_name   = int(request.GET.get('upozilla_name', None))
#     upozilla_wise_post = models.PostOfficeInfo.objects.filter(upozilla_name_id = upozilla_name)
    
#     context = {
#         'upozilla_wise_post': upozilla_wise_post,
#     }
#     return render(request, 'durbarapp/bind_post_office.html', context)



