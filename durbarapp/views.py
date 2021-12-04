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

############################### Website view START #################################
def homepage(request):
    if request.POST:
        if request.is_ajax():
            marchant_name = request.POST.get('marchant_name')
            contact_no1 = request.POST.get('contact_no1')
            password = request.POST.get('password')
            district_name = request.POST.get('programming_id')
            upazilla_name = request.POST.get('courses_id')
            models.MerchantInfo.objects.create(
                marchant_name = marchant_name,
                contact_no1 = contact_no1,
                password = password,
                district_name_id = district_name,
                upazilla_name_id = upazilla_name,
            )
            return JsonResponse("Submit Completed", safe = False)  
 

    services = models.Service.objects.filter(status=True).order_by('id')
    best = models.WhyBest.objects.filter(status=True).order_by('id')
    deliverycharge = models.DeliveryCharge.objects.filter(status=True).order_by('delivery_charge_location_id')

    context={
        'services':services,
        'best':best,
        'deliverycharge':deliverycharge,
    }
    return render (request, 'durbarapp/index.html',context)





############################### Website view END #################################

















############################### Merchant view START #################################

def merchant_login(request):
    
    if request.is_ajax():
        contact_no1 = request.GET.get('contact_no1')
        password = request.GET.get('password')
        user = models.MerchantInfo.objects.filter(contact_no1 = contact_no1,password = password).first()
        if user:
            
            request.session['id'] = user.id
            data = "success"
            return JsonResponse(data, safe = False)
        else:
            
            messages.warning(request, "Wrong Information")
            return redirect("/")
       
            


def merchant_dashboard(request): 
    # if request.session['id'] == False:
    #     return redirect('merchant-login')
     

    return render (request, 'merchant_dashboard_v2/index.html')



 
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

        packegeType = int(request.POST[('packegeType')])
        collection_time_category = int(request.POST[('collection_time_category')])
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
            packegeType_id = packegeType,
            collection_time_category_id = collection_time_category,

            )
        return redirect('/order-list/')
    return render (request, 'merchant_dashboard_v2/newOrder2.html')



def order_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(merchant_info_id = request.session['id']).order_by('created')
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'merchant_dashboard_v2/orderList.html',context)



def service_charge_list(request):
    order = models.MerchantOrder.objects.filter(merchant_info_id = request.session['id']).order_by('id')
    context={
        "order":order,
    }
    return render(request, 'merchant_dashboard/serviceCharge.html',context)


def customer_info_edit(request): 
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




############################### Merchant view END #################################
















############################### Admin view START #################################





def admin_dashboard(request): 
    all_count = models.MerchantOrder.objects.all().count()
    pending_count = models.MerchantOrder.objects.filter(order_track = "1").count()
    assign_for_pick_count = models.MerchantOrder.objects.filter(order_track = "2").count()
    picked_count = models.MerchantOrder.objects.filter(order_track = "3").count()
    hub_collected_for_ware_house_count = models.MerchantOrder.objects.filter(order_track = "4").count()
    in_transit_count = models.MerchantOrder.objects.filter(order_track = "5").count()
    hub_collected_for_delevery_count = models.MerchantOrder.objects.filter(order_track = "6").count()
    assign_for_delevery_count = models.MerchantOrder.objects.filter(order_track = "7").count()
    shiping_count = models.MerchantOrder.objects.filter(order_track = "8").count()
    delivered_count = models.MerchantOrder.objects.filter(order_track = "9").count()
    hold_count = models.MerchantOrder.objects.filter(order_track = "10").count()
    return_pending_count = models.MerchantOrder.objects.filter(order_track = "11").count()
    return_to_hub_for_ware_house_count = models.MerchantOrder.objects.filter(order_track = "12").count()
    hub_returned_to_ware_house_count = models.MerchantOrder.objects.filter(order_track = "13").count()
    return_to_hub_count = models.MerchantOrder.objects.filter(order_track = "14").count()
    assign_for_return_count = models.MerchantOrder.objects.filter(order_track = "15").count()
    picked_for_return_count = models.MerchantOrder.objects.filter(order_track = "16").count()
    return_to_merchent_count = models.MerchantOrder.objects.filter(order_track = "17").count()
    canceled_count = models.MerchantOrder.objects.filter(order_track = "18").count()
    context={
        "all_count":all_count,
        "assign_for_pick_count":assign_for_pick_count,
        "hub_collected_for_ware_house_count":hub_collected_for_ware_house_count,
        "hub_collected_for_delevery_count":hub_collected_for_delevery_count,
        "assign_for_delevery_count":assign_for_delevery_count,
        "shiping_count":shiping_count,
        "return_to_hub_for_ware_house_count":return_to_hub_for_ware_house_count,
        "hub_returned_to_ware_house_count":hub_returned_to_ware_house_count,
        "assign_for_return_count":assign_for_return_count,
        "picked_for_return_count":picked_for_return_count,
        "pending_count":pending_count,
        "picked_count":picked_count,
        "in_transit_count":in_transit_count,
        "delivered_count":delivered_count,
        "hold_count":hold_count,
        "return_pending_count":return_pending_count,
        "return_to_hub_count":return_to_hub_count,
        "return_to_merchent_count":return_to_merchent_count,
        "canceled_count":canceled_count,
    }
     

    return render (request, 'durbar_admin_panel/index.html',context)




def all_order_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.all().order_by('created')
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/all_order.html',context)

def pending_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="1")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/pending_list.html',context)

def assign_for_pick_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="2")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/assign_for_pick_list.html',context)

def picked_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="3")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/picked_list.html',context)

def hub_collected_for_ware_house_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.all().filter(order_track="4")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/hub_collected_for_ware_house_list.html',context)

def in_transit_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="5")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/in_transit_list.html',context)

def hub_collected_for_delevery_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="6")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/hub_collected_for_delevery_list.html',context)

def assign_for_delevery_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="7")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/assign_for_delevery_list.html',context)

def shiping_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="8")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/shiping_list.html',context)

def delivered_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="9")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/delivered_list.html',context)

def hold_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="10")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/hold_list.html',context)

def return_pending_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="11")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/return_pending_list.html',context)

def return_to_hub_for_ware_house_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="12")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/return_to_hub_for_ware_house_list.html',context)

def hub_returned_to_ware_house_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="13")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/hub_returned_to_ware_house_list.html',context)

def return_to_hub_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="14")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/return_to_hub_list.html',context)

def assign_for_return_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="15")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/assign_for_return_list.html',context)

def picked_for_return_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="16")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/picked_for_return_list.html',context)

def return_to_merchent_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="17")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/return_to_merchent_list.html',context)

def canceled_list(request):
    dislist = models.DistrictEntry.objects.all()
    order = models.MerchantOrder.objects.filter(order_track="18")
    context={
        "order":order,
        "dislist":dislist,
        
    }
    return render(request, 'durbar_admin_panel/canceled_list.html',context)



def order_upgrade(request,id):
    main_data    = models.MerchantOrder.objects.get(order_id = id)
    



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

        packegeType = int(request.POST[('packegeType')])
        collection_time_category = int(request.POST[('collection_time_category')])
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
            
            packegeType_id = packegeType,
            collection_time_category_id = collection_time_category,

            )
        return redirect('/order-list/')
    context={
        'main_data':main_data
    }
    return render (request, 'durbar_admin_panel/upgrade_order.html',context)

def add_hub(request):
    try:
        data = models.HubInfo.objects.latest("hub_id")
        str_data = str(data)
        past_id = str_data[2:]
        past_id=int(past_id)
        new_id = past_id+1
        new_id = '{0:04d}'.format(new_id)
        no=str('H-')+str(new_id)
        hub_id = no
    except:
        hub_no = '{0:04d}'.format(1)
        no=str('H-')+str(hub_no)
        hub_id = no

    if request.method == 'POST':
        hub_owner_name = request.POST.get('hub_owner_name')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        bank_name = request.POST.get('bank_name')
        bank_ac_no = request.POST.get('bank_ac_no')
        bank_branch_name = request.POST.get('bank_branch_name')
        mobile_banking_no = request.POST.get('mobile_banking_no')
        trade_license_no = request.POST.get('trade_license_no')
        

        mobile_banking_category = int(request.POST[('mobile_banking_category')])
        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])


        models.HubInfo.objects.create(
            hub_owner_name = hub_owner_name,
            email = email ,
            password = password,  
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2, 
            present_address = present_address, 
            permanent_address = permanent_address, 
            bank_name = bank_name, 
            
            bank_ac_no =  bank_ac_no,
            bank_branch_name = bank_branch_name,
            mobile_banking_no = mobile_banking_no,
            trade_license_no = trade_license_no, 
            
            district_name_id = district_name, 
            upazilla_name_id = upazilla_name, 
            mobile_banking_category_id = mobile_banking_category, 
            hub_id = hub_id, 
           

            )
        return redirect('/order-list/')
    
    return render (request, 'durbar_admin_panel/add_hub.html')