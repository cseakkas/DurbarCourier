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
import random

def homepage(request):
    
    return render (request, 'durbarapp/index.html')

def merchant_login(request):
    if request.method=="POST":  
        login_data = models.MerchantInfo.objects.filter(email = request.POST['email'], password = request.POST['password'] )  
        if login_data:
            request.session['userid'] = login_data[0].id 
            return redirect('/merchant-dashboard/')
        else:
            return redirect('/')

    return render (request, 'durbarapp/merchant_login.html')

def merchant_dashboard(request): 
    if request.session['userid'] == False:
        return redirect('/')
     

    return render (request, 'merchant_dashboard/index.html')

 
def merchant_logout(request):
    request.session['userid'] = False
    return redirect('/')







