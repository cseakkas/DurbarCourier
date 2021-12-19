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



############################### Merchant view START #################################

def merchant_login(request):
    
    if request.is_ajax():
        contact_no1 = request.GET.get('contact_no1')
        password = request.GET.get('password')
        user = models.MerchantInfo.objects.filter(contact_no1 = contact_no1,password = password, status=True).first()
        if user:
            
            request.session['id'] = user.id
            request.session['merchant_id'] = user.merchant_id
            request.session['merchant_name'] = user.marchant_name
            data = "success"
            return JsonResponse(data, safe = False)
        else:
            
            messages.warning(request, "Wrong Information")
            return redirect("/")
       
            


def merchant_dashboard(request): 
    # if request.session['id'] == False:
    #     return redirect('merchant-login')
     

    return render (request, 'merchant_dashboard_v2/index.html')


def merchant_profile(request): 
    if request.session.get('merchant_id') == False:
        return redirect("/")
    profile_info = models.MerchantInfo.objects.filter(merchant_id = request.session['merchant_id'], status=True).first()
    collection_location = models.PickupLocation.objects.filter(merchant_id__merchant_id = request.session['merchant_id'], status=True)
    
    context={
        "profile_info":profile_info,
        "collection_location":collection_location,
    }

    return render (request, 'merchant_dashboard_v2/profile.html',context)



 
def merchant_logout(request):
    request.session['merchant_id'] = False
    return redirect('/')


 

def load_courses(request):
    district_name_id = request.GET.get('programming')
    courses = models.UpazillaEntry.objects.filter(district_name_id = district_name_id).order_by('district_name')
    return render(request, 'merchant_dashboard/courses_dropdown_list_options.html', {'courses': courses})


 

def load_post(request):
    upazilla_name_id = request.GET.get('courses')
    post = models.PostOfficeInfo.objects.filter(upazilla_name_id = upazilla_name_id).order_by('id')
    return render(request, 'merchant_dashboard/post_dropdown_list_options.html', {'post': post})


 

def load_hub(request):
    upazilla_name_id = request.GET.get('courses3')
    post = models.HubInfo.objects.filter(upazilla_name_id = upazilla_name_id).order_by('id')
    return render(request, 'merchant_dashboard/hub_dropdown_list_options..html', {'post': post})



 

def load_weight(request):
    dstrict_id = request.GET.get('programming')
    get_district = models.DistrictEntry.objects.filter(id = dstrict_id).first()
    chk_inOut = get_district.is_inside_dhaka
    weight_list = models.DeliveryCharge.objects.filter(delivery_charge_location__id = chk_inOut).order_by('id')
    merchant_wise = models.DeliveryCharge_by_Merchant.objects.filter(merchant_id__merchant_id = request.session.get('merchant_id'),delivery_charge_location__id = chk_inOut).order_by('id')
    
    context={
        'weight_list': weight_list,
        'merchant_wise':merchant_wise
    }
    return render(request, 'merchant_dashboard/load_weight.html', context)

 

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
    if request.session.get('merchant_id') == False:
        return redirect("/")
    
    get_dist = models.MerchantInfo.objects.filter(merchant_id =  request.session.get('merchant_id')).first()
    marchant_district_id = get_dist.district_name.id
    pickup           = models.PickupLocation.objects.filter(merchant_id__merchant_id = request.session['merchant_id'] , status = True) 
    
    delevery_charge  = models.DeliveryCharge.objects.filter(status = True).order_by("id")
    # delevery_charge  = models.DeliveryChargeWeight.objects.filter(status = True).order_by("-id")
    # delevery_charge_by_merchant  = models.DeliveryChargeWeight.objects.filter(merchant_id__merchant_id = request.session['merchant_id'] ,status = True).order_by("-id")
    try:
        data = models.MerchantOrder.objects.latest("rider_id")
        str_data = str(data)
        past_id = str_data[3:]
        past_id=int(past_id)
        new_id = past_id+1
        new_id = '{0:04d}'.format(new_id)
        no=str('DC-')+str(new_id)
        converted_num = no
        
    except:
        hub_no = '{0:04d}'.format(1)
        no=str('DC-')+str(hub_no)
        converted_num = no
     

    # alldata = models.MerchantOrder.objects.all().exists()

    if request.is_ajax():
        weight_cost_id = request.GET.get('weight_cost_id') 
        results = []
        
        get_cost_marchant = models.DeliveryCharge_by_Merchant.objects.filter(id = weight_cost_id).first()
        if get_cost_marchant: 
            get_data = { 
                'get_cost':get_cost_marchant.cost    
            }
        else: 
            get_cost_marchant = models.DeliveryCharge.objects.filter(id = weight_cost_id).first()
            get_data = { 
                'get_cost':get_cost_marchant.cost    
            }
         
        results.append(get_data) 
        return JsonResponse(results, safe = False)


    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        address = request.POST.get('address')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        reference_no = request.POST.get('reference_no')
        actual_package_price = request.POST.get('actual_package_price')
        collection_date = request.POST.get('collection_date')
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

        packegeType = request.POST.get('packegeType')
        collection_time_category = int(request.POST[('collection_time_category')])
        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])
        post_office_name = int(request.POST[('post_office_name')])
        pickup_location = int(request.POST[('pickup_location')])

        models.MerchantOrder.objects.create(
            merchant_info_id = int(request.session['id']),
            customer_name = customer_name ,
            address = address,  
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2, 
            reference_no = reference_no, 
            actual_package_price = actual_package_price, 
            collection_date = collection_date, 
            
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
            pickup_location_id = pickup_location, 
            order_id = converted_num,
            packegeType = packegeType,
            collection_time_category_id = collection_time_category,

            )
        return redirect('/order-list/')
    context={
        'pickup' : pickup,
        'delevery_charge' : delevery_charge,
        # 'delevery_charge_by_merchant' : delevery_charge_by_merchant,
    }
    return render (request, 'merchant_dashboard_v2/newOrder.html',context)



def order_list(request):
    if request.session.get('merchant_id') == False:
        return redirect("/")
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(merchant_info_id = request.session['id']).order_by('created')
    context={
        "order":order,
        "dislist":dislist, 
    }
    return render(request, 'merchant_dashboard_v2/orderList.html',context)



def service_charge_list(request):
    if request.session.get('merchant_id') == False:
        return redirect("/")
    order = models.MerchantOrder.objects.filter(merchant_info_id = request.session['id']).order_by('id')
    context={
        "order":order,
    }
    return render(request, 'merchant_dashboard/serviceCharge.html', context)

def marchant_order_tracking(request):
    if request.session.get('merchant_id') == False:
        return redirect("/")
    order = models.MerchantOrder.objects.filter(merchant_info_id = request.session['id']).order_by('id')
    context={
        "order":order,
    }
    return render(request, 'merchant_dashboard_v2/marchant_order_tracking.html', context)


def customer_info_edit(request): 
    if request.session.get('merchant_id') == False:
        return redirect("/")
    if request.is_ajax():
        customer_id = request.GET.get('CusId')
        get_cus = models.MerchantOrder.objects.filter(order_id = customer_id).first()
        
        dislist = models.DistrictEntry.objects.all()

        results = []
        get_data = { 
            'customer_name':get_cus.customer_name,
            'address':get_cus.address,
            'contact_no1':get_cus.contact_no1,
            'collection_amount':get_cus.collection_amount,   
            'district_name_id':str(get_cus.district_name),   
            # 'dislist':str(dislist),   
           
        }

        results.append(get_data)
         
        return JsonResponse(results, safe = False)






