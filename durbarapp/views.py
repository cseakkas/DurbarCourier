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
    if request.method == 'POST':
        marchant_name = request.POST.get('marchant_name')
        address = request.POST.get('address')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        logo = ""
        if bool(request.FILES.get('logo', False)) == True:
            file = request.FILES['logo']
            logo = "merchant_register/"+file.name
            if not os.path.exists(settings.MEDIA_ROOT+"merchant_register/"):
                os.mkdir(settings.MEDIA_ROOT+"merchant_register/")
            default_storage.save(settings.MEDIA_ROOT+"merchant_register/"+file.name, ContentFile(file.read()))

        email = request.POST.get('email')
        password = request.POST.get('password')
        new_md5_obj     = hashlib.md5(password.encode())
        new_enc_pass    = new_md5_obj.hexdigest() 

        check_user = models.MerchantInfo.objects.filter(email = email).first()
        
        if check_user:
            messages.warning(request, "User already exist")
            return render(request,'durbarapp/merchant_login.html' )
            
        models.MerchantInfo.objects.create(
            email = email ,
            marchant_name = marchant_name, 
            address = address, 
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2, 
            logo = logo, 
           
            password = new_enc_pass
            )
        messages.success(request, "Registration Successfull") 
    return render (request, 'durbarapp/register.html')

def merchant_dashboard(request): 
    if request.session['id'] == False:
        return redirect('merchant-login')
     

    return render (request, 'merchant_dashboard/index.html')

 
def merchant_logout(request):
    request.session['id'] = False
    return redirect('/')







