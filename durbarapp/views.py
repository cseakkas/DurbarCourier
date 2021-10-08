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
    services = models.Service.objects.filter(status=True).order_by('id')
    best = models.WhyBest.objects.filter(status=True).order_by('id')
    deliverycharge = models.DeliveryCharge.objects.filter(status=True).order_by('delivery_charge_location_id')

    context={
        'services':services,
        'best':best,
        'deliverycharge':deliverycharge,
    }
    return render (request, 'durbarapp/index.html',context)

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
            logo = "merchant_logo/"+file.name
            if not os.path.exists(settings.MEDIA_ROOT+"merchant_logo/"):
                os.mkdir(settings.MEDIA_ROOT+"merchant_logo/")
            default_storage.save(settings.MEDIA_ROOT+"merchant_logo/"+file.name, ContentFile(file.read()))

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
        return redirect('/merchant-login/')
    return render (request, 'durbarapp/register.html')

def merchant_dashboard(request): 
    if request.session['id'] == False:
        return redirect('merchant-login')
     

    return render (request, 'merchant_dashboard/index.html')

 
def merchant_logout(request):
    request.session['id'] = False
    return redirect('/')


 

def load_courses(request):
    district_name_id = request.GET.get('programming')
    courses = models.UpazillaEntry.objects.filter(district_name_id = district_name_id).order_by('district_name')
    return render(request, 'merchant_dashboard/courses_dropdown_list_options.html', {'courses': courses})


 

def load_post(request):
    upazilla_name_id = request.GET.get('courses')
    post = models.PostOfficeInfo.objects.filter(upazilla_name_id = upazilla_name_id).order_by('id')
    return render(request, 'merchant_dashboard/post_dropdown_list_options.html', {'post': post})



 

def load_weight(request):
    area_id = request.GET.get('locationCollection')
    post = models.DeliveryCharge.objects.filter(collection_point_id = area_id).order_by('id')
    return render(request, 'merchant_dashboard/load_weight.html', {'post': post})

 

def load_cost(request):
    weightid = request.GET.get('weight')
    areaId = request.GET.get('areaId')

    post = models.DeliveryCharge.objects.filter(collection_point_id=areaId, delivery_charge_weight_id = weightid)
    
    place_json = {}
    results = [] 
    place_json['shipment_charge'] = post[0].cost    
    results.append(place_json) 

    return JsonResponse(results, safe=False)





def new_order(request):
    try:
        data = models.MerchantOrder.objects.latest("order_id")
        sampleDate = datetime.date.today()
        dateFormatted = sampleDate.strftime("%y""%m")
        data = int(data.order_id)
        str1 = str(data)
        month = str1[0:4]
        if dateFormatted == month:
            order_no = data+1
            converted_num = int(order_no)
        else:
            order_no = '{0:04d}'.format(1)
            no=str(dateFormatted)+str(order_no)
            converted_num = int(no)
    except:
        sampleDate = datetime.date.today()
        dateFormatted = sampleDate.strftime("%y""%m")
        order_no = '{0:04d}'.format(1)
        no=str(dateFormatted)+str(order_no)
        converted_num = int(no)   

    # alldata = models.MerchantOrder.objects.all().exists()



    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        address = request.POST.get('address')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        reference_no = request.POST.get('reference_no')
        actual_package_price = request.POST.get('actual_package_price')
        collection_date = request.POST.get('collection_date')
        collection_time = request.POST.get('collection_time')
        only_delivery = True if request.POST.get('only_delivery') else False
        delivery_and_amount_collection = True if request.POST.get('delivery_and_amount_collection') else False
        lequed_or_Fragile = True if request.POST.get('lequed_or_Fragile') else False
        weight = int(request.POST[('weight')])
        addtional_note = request.POST.get('addtional_note')
        collection_amount = request.POST.get('collection_amount')
        total_service_charge = request.POST.get('total_service_charge')
        lequed_or_Fragile_charge = request.POST.get('lequed_or_Fragile_charge')
        cod_charge = request.POST.get('cod_charge')
        shipment_charge = request.POST.get('shipment_charge')

        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])
        post_office_name = int(request.POST[('post_office_name')])
        collection_point = int(request.POST[('collection_point')])

        models.MerchantOrder.objects.create(
            merchant_info_id = int(request.session['id']),
            customer_name = customer_name ,
            address = address,  
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2, 
            reference_no = reference_no, 
            actual_package_price = actual_package_price, 
            collection_date = collection_date, 
            collection_time = collection_time,
            only_delivery =  only_delivery,
            delivery_and_amount_collection = delivery_and_amount_collection,
            lequed_or_Fragile = lequed_or_Fragile,
            weight_id = weight, 
            collection_amount = collection_amount, 
            total_service_charge = total_service_charge, 
            lequed_or_Fragile_charge = lequed_or_Fragile_charge, 
            cod_charge = cod_charge, 
            shipment_charge = shipment_charge, 
            addtional_note = addtional_note, 
            district_name_id = district_name, 
            upazilla_name_id = upazilla_name, 
            post_office_name_id = post_office_name, 
            collection_point_id = collection_point, 
            order_id = converted_num,

            )
        return redirect('/order-list/')
    return render (request, 'merchant_dashboard/newOrder.html')



def order_list(request):
    order = models.MerchantOrder.objects.filter(merchant_info_id = request.session['id']).order_by('id')
    context={
        "order":order,
    }
    return render(request, 'merchant_dashboard/orderList.html',context)



def service_charge_list(request):
    order = models.MerchantOrder.objects.filter(merchant_info_id = request.session['id']).order_by('id')
    context={
        "order":order,
    }
    return render(request, 'merchant_dashboard/serviceCharge.html',context)

