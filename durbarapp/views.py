from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.http import HttpResponse, response
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
    try:
        data = models.MerchantInfo.objects.latest("merchant_id")
        str_data = str(data)
        past_id = str_data[2:]
        past_id=int(past_id)
        new_id = past_id+1
        new_id = '{0:04d}'.format(new_id)
        no=str('M-')+str(new_id)
        merchant_id = no 
    except:
        hub_no = '{0:04d}'.format(1)
        no=str('M-')+str(hub_no)
        merchant_id = no
        
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
                merchant_id = merchant_id,
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


def update_upazilla(request): 
    district_id = request.GET.get('district_id') 
    get_up_id = int(request.GET.get('get_up_id')) 
    
    upozilla_list = models.UpazillaEntry.objects.filter(district_name_id = district_id).order_by('district_name')

    context = {
        'upozilla_list':upozilla_list,
        'get_up_id':get_up_id,
    }
    return render(request, 'durbar_admin_panel/distirct_wise_upozilla.html', context)




def select_hub(request): 
    upozilla_id = request.GET.get('upozilla_id') 
     
    
    hub_list = models.HubInfo.objects.filter(upazilla_name_id = upozilla_id).order_by('district_name')

    context = {
        'hub_list':hub_list,
        
    }
    return render(request, 'durbar_admin_panel/select_upazilla_wise_hub.html', context)


def update_hub(request): 
    upozilla_id = request.GET.get('upozilla_id') 
    hub_id = int(request.GET.get('hub_id')) 
    
    hub_list = models.HubInfo.objects.filter(upazilla_name_id = upozilla_id).order_by('district_name')

    context = {
        'hub_list':hub_list,
        'hub_id':hub_id,
    }
    return render(request, 'durbar_admin_panel/upazilla_wise_hub.html', context)





def invoice_print(request,order_id): 
    
    invoice = models.MerchantOrder.objects.filter(order_id = order_id).first()
    
    context = {
        'invoice':invoice,
        
    }
    return render(request, 'durbar_hub_panel/invoice.html', context)


























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
        owner_nid = request.POST.get('owner_nid')
        address = request.POST.get('address')
        bank_name = request.POST.get('bank_name')
        bank_ac_no = request.POST.get('bank_ac_no')
        bank_branch_name = request.POST.get('bank_branch_name')
        mobile_banking_no = request.POST.get('mobile_banking_no')
        trade_license_no = request.POST.get('trade_license_no')
        owner_image = ""
        if bool(request.FILES.get('owner_image', False)) == True:
            file = request.FILES['owner_image']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            owner_image = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if owner_image:
                owner_image = str("hub_doc/")+str(owner_image).split("/")[-1]
            
        owner_nid_image = ""
        if bool(request.FILES.get('owner_nid_image', False)) == True:
            file = request.FILES['owner_nid_image']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            owner_nid_image = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if owner_nid_image:
                owner_nid_image = str("hub_doc/")+str(owner_nid_image).split("/")[-1]
            
        owner_tin = ""
        if bool(request.FILES.get('owner_tin', False)) == True:
            file = request.FILES['owner_tin']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            owner_tin = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if owner_tin:
                owner_tin = str("hub_doc/")+str(owner_tin).split("/")[-1]
            
        trade_license = ""
        if bool(request.FILES.get('trade_license', False)) == True:
            file = request.FILES['trade_license']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            trade_license = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if trade_license:
                trade_license = str("hub_doc/")+str(trade_license).split("/")[-1]
            
        mobile_banking_category = int(request.POST[('mobile_banking_category')])
        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])


        models.HubInfo.objects.create(
            hub_owner_name = hub_owner_name,
            email = email ,
            password = password,  
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2, 
            address = address,  
            bank_name = bank_name, 
            nid = owner_nid, 
            
            bank_ac_no =  bank_ac_no,
            bank_branch_name = bank_branch_name,
            mobile_banking_no = mobile_banking_no,
            trade_license_no = trade_license_no, 
            owner_image = owner_image, 
            owner_nid_image = owner_nid_image, 
            owner_tin = owner_tin, 
            trade_license = trade_license, 
            
            district_name_id = district_name, 
            upazilla_name_id = upazilla_name, 
            mobile_banking_category_id = mobile_banking_category, 
            hub_id = hub_id, 
           

            )
        
    
    return render (request, 'durbar_admin_panel/add_hub.html')


def add_rider(request):
    try:
        data = models.RiderInfo.objects.latest("rider_id")
        str_data = str(data)
        past_id = str_data[2:]
        past_id=int(past_id)
        new_id = past_id+1
        new_id = '{0:04d}'.format(new_id)
        no=str('R-')+str(new_id)
        rider_id = no
        
    except:
        hub_no = '{0:04d}'.format(1)
        no=str('R-')+str(hub_no)
        rider_id = no
        

    if request.method == 'POST':
        rider_name = request.POST.get('rider_name')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        email = request.POST.get('email')
        password = request.POST.get('password')
        owner_nid = request.POST.get('owner_nid')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        bank_name = request.POST.get('bank_name')
        bank_ac_no = request.POST.get('bank_ac_no')
        bank_branch_name = request.POST.get('bank_branch_name')
        mobile_banking_no = request.POST.get('mobile_banking_no')
        
        
        
        rider_image = ""
        if bool(request.FILES.get('rider_image', False)) == True:
            file = request.FILES['rider_image']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            rider_image = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if rider_image:
                rider_image = str("hub_doc/")+str(rider_image).split("/")[-1]
            
        rider_nid_image = ""
        if bool(request.FILES.get('rider_nid_image', False)) == True:
            file = request.FILES['rider_nid_image']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            rider_nid_image = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if rider_nid_image:
                rider_nid_image = str("hub_doc/")+str(rider_nid_image).split("/")[-1]
            
        hub = int(request.POST[('hub')]) 
        mobile_banking_category = int(request.POST[('mobile_banking_category')])
        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])
        
        models.RiderInfo.objects.create(
            rider_name = rider_name,
            email = email ,
            password = password,  
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2, 
            present_address = present_address,  
            permanent_address = permanent_address,  
            bank_name = bank_name, 
            nid = owner_nid, 
            
            bank_ac_no =  bank_ac_no,
            bank_branch_name = bank_branch_name,
            mobile_banking_no = mobile_banking_no,
            
            rider_image = rider_image, 
            rider_nid_image = rider_nid_image, 
            hub_id = hub, 
            district_name_id = district_name, 
            upazilla_name_id = upazilla_name, 
            mobile_banking_category_id = mobile_banking_category, 
            rider_id = rider_id, 

            )
        return redirect('/rider-list/')

    return render (request, 'durbar_admin_panel/add_rider.html')


def rider_update(request, rider_id): 
    main_data    = models.RiderInfo.objects.filter(rider_id = rider_id).first()
    district_id = main_data.district_name.id
    upazilla_id = main_data.upazilla_name.id
    hub_id = main_data.hub.id
    

    if request.method == 'POST':
        rider_name = request.POST.get('rider_name')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        email = request.POST.get('email')
        password = request.POST.get('password')
        owner_nid = request.POST.get('owner_nid')
        present_address = request.POST.get('present_address')
        permanent_address = request.POST.get('permanent_address')
        bank_name = request.POST.get('bank_name')
        bank_ac_no = request.POST.get('bank_ac_no')
        bank_branch_name = request.POST.get('bank_branch_name')
        mobile_banking_no = request.POST.get('mobile_banking_no')
        
        
        hublist = request.POST.getlist('hub')
        if main_data.rider_image:  
            rider_image = main_data.rider_image
        else:
            rider_image = " "
        if bool(request.FILES.get('rider_image', False)) == True:
            file = request.FILES['rider_image']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            rider_image = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if rider_image:
                rider_image = str("hub_doc/")+str(rider_image).split("/")[-1]
            
        rider_nid_image = ""
        if bool(request.FILES.get('rider_nid_image', False)) == True:
            file = request.FILES['rider_nid_image']   
            if not os.path.exists(settings.MEDIA_ROOT+"hub_doc/"):
                os.mkdir(settings.MEDIA_ROOT+"hub_doc/")

            rider_nid_image = default_storage.save("hub_doc/"+file.name, ContentFile(file.read()))
            if rider_nid_image:
                rider_nid_image = str("hub_doc/")+str(rider_nid_image).split("/")[-1]
            
            
        mobile_banking_category = int(request.POST[('mobile_banking_category')])
        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])
        
        for hub in hublist:
            models.RiderInfo.objects.filter(rider_id = rider_id).update(
                rider_name = rider_name,
                email = email ,
                password = password,  
                contact_no1 = contact_no1, 
                contact_no2 = contact_no2, 
                present_address = present_address,  
                permanent_address = permanent_address,  
                bank_name = bank_name, 
                nid = owner_nid, 
                
                bank_ac_no =  bank_ac_no,
                bank_branch_name = bank_branch_name,
                mobile_banking_no = mobile_banking_no,
                
                rider_image = rider_image, 
                rider_nid_image = rider_nid_image, 
                hub_id = int(hub), 
                district_name_id = district_name, 
                upazilla_name_id = upazilla_name, 
                mobile_banking_category_id = mobile_banking_category, 
                

                )
    
    context={
        'main_data' : main_data,
    }
    return render (request, 'durbar_admin_panel/rider_update.html',context)


def hub_list(request):
    
    hub_list = models.HubInfo.objects.filter(status=True)
    context={
        "hub_list":hub_list,
        
    }
    return render(request, 'durbar_admin_panel/hub_list.html',context)

def rider_list(request):
    
    rider_list = models.RiderInfo.objects.raw(" SELECT r.id, r.rider_id, r.hub_id, h.id, h.hub_id, GROUP_CONCAT(h.hub_id SEPARATOR ', ') as hub_name FROM durbarapp_riderinfo r LEFT JOIN durbarapp_hubinfo h ON r.hub_id = h.id GROUP BY r.rider_id ")
    context={
        "rider_list":rider_list,
        
    }
    return render(request, 'durbar_admin_panel/rider_list.html',context)


def merchent_request(request):
    
    request_list = models.MerchantInfo.objects.filter(status=False).order_by("created")
    context={
        "request_list":request_list,
        
    }
    return render(request, 'durbar_admin_panel/merchant_request.html',context)




def merchant_approval(request,id):

    main_data = models.MerchantInfo.objects.filter(id=id,status=False).first()

    if request.method == 'POST':
        marchant_name = request.POST.get('marchant_name')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        bank_name = request.POST.get('bank_name')
        bank_ac_no = request.POST.get('bank_ac_no')
        bank_branch_name = request.POST.get('bank_branch_name')
        mobile_banking_no = request.POST.get('mobile_banking_no')
        
        
        hub = int(request.POST[('hub')])
        mobile_banking_category = int(request.POST[('mobile_banking_category')])
        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])
        



        models.MerchantInfo.objects.filter(id = id).update(
            marchant_name = marchant_name,
            email = email ,
            password = password,  
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2,  
            address = address,  
            bank_name = bank_name, 
            bank_ac_no =  bank_ac_no,
            bank_branch_name = bank_branch_name,
            mobile_banking_no = mobile_banking_no,
            hub_id = hub, 
            district_name_id = district_name, 
            upazilla_name_id = upazilla_name, 
            mobile_banking_category_id = mobile_banking_category, 
            status = "True"
            )
        models.PickupLocation.objects.create(
            hub_id = hub, 
            district_name_id = district_name, 
            upazilla_name_id = upazilla_name, 
            merchant_id = id,
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2,  
            address = address,
            status = "True"
            )
        return redirect('/merchant-request')
    context={
        "main_data":main_data,
        
    }
    return render(request, 'durbar_admin_panel/merchant_approval.html',context)


def merchant_management_list(request):
    
    merchant_list = models.MerchantInfo.objects.filter(status=True)
    context={
        "merchant_list":merchant_list,
        
    }
    return render(request, 'durbar_admin_panel/merchant_management_list.html',context)


def merchant_management_edit(request,id):

    main_data = models.MerchantInfo.objects.filter(merchant_id = id).first()
    pickup_location_data = models.PickupLocation.objects.filter(merchant_id__merchant_id = id,status=True).all()

    if request.method == 'POST':
        marchant_name = request.POST.get('marchant_name')
        contact_no1 = request.POST.get('contact_no1')
        contact_no2 = request.POST.get('contact_no2')
        email = request.POST.get('email')
        password = request.POST.get('password')
        address = request.POST.get('address')
        bank_name = request.POST.get('bank_name')
        bank_ac_no = request.POST.get('bank_ac_no')
        bank_branch_name = request.POST.get('bank_branch_name')
        mobile_banking_no = request.POST.get('mobile_banking_no')
        
        
        hub = int(request.POST[('hub')])
        mobile_banking_category = int(request.POST[('mobile_banking_category')])
        district_name = int(request.POST[('district_name')])
        upazilla_name = int(request.POST[('upazilla_name')])
        



        models.MerchantInfo.objects.filter(id = id).update(
            marchant_name = marchant_name,
            email = email ,
            password = password,  
            contact_no1 = contact_no1, 
            contact_no2 = contact_no2,  
            address = address,  
            bank_name = bank_name, 
            bank_ac_no =  bank_ac_no,
            bank_branch_name = bank_branch_name,
            mobile_banking_no = mobile_banking_no,
            hub_id = hub, 
            district_name_id = district_name, 
            upazilla_name_id = upazilla_name, 
            mobile_banking_category_id = mobile_banking_category, 
            status = "True"
            )
        return redirect('/merchant-request')
    context={
        "main_data":main_data,
        "pickup_location_data":pickup_location_data,
        
    }
    return render(request, 'durbar_admin_panel/merchant_management_edit.html',context)













############################### Admin view END #################################









############################### HUB view Start #################################



def hub_login(request):
    if request.method=="POST":
        contact_no1     = request.POST['contact_no1']
        password  = request.POST['password']

        user        = models.HubInfo.objects.filter(contact_no1 = contact_no1, password = password)
        if user:
            request.session['contact_no1'] = user[0].contact_no1
            request.session['hub_id'] = user[0].hub_id
            request.session['h_id'] = user[0].id
            return redirect("/hub-dashboard/")
        else:
            messages.warning(request, "Wrong Information")
    return render(request, "durbar_hub_panel/hub_login.html")  
            
 
def hub_logout(request):
    request.session['hub_id'] = False
    return redirect('/hub')


def hub_dashboard(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    return render(request, "durbar_hub_panel/index.html")  
            


def hub_pending_list(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    pending_data = models.MerchantOrder.objects.filter(pickup_location__hub__hub_id = request.session['hub_id'],order_track=1).order_by("id")
    
    context={
        'pending_data':pending_data,
        
    }

    return render(request, "durbar_hub_panel/pending_list.html",context)  
            

def hub_pending_update(request,id):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    pending_data = models.MerchantOrder.objects.filter(pickup_location_id = id,order_track="1").first()
    all_order = models.MerchantOrder.objects.filter(pickup_location_id = id,order_track="1").all()
    pending_data_count = models.MerchantOrder.objects.filter(pickup_location_id = id,order_track="1").count()
    riders_for_hub = models.RiderInfo.objects.filter(hub_id__hub_id = request.session['hub_id']).all()
    print(all_order)
    if request.method=="POST":
        rider = int(request.POST[('rider')])
        for i in all_order:
            models.RiderOrder.objects.create(
                order_info_id = i.id,
                rider_id = rider,
                pickup_location_id = i.pickup_location.id,

                )
        for i in all_order:
            models.MerchantOrder.objects.filter(order_id = i.order_id).update(
            order_track = "2",
            hub_rider_assign_for_pick_time = datetime.datetime.now()
            

            )
            
        return redirect("/hub-pending")

    context={
        'pending_data':pending_data,
        'pending_data_count':pending_data_count,
        'riders_for_hub':riders_for_hub,
    }

    return render(request, "durbar_hub_panel/hub_rider_assign.html",context)  
            


def hub_picking_from_rider_list(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    picked_data = models.RiderOrder.objects.filter(rider_id__hub_id__hub_id = request.session['hub_id'],picked = True).order_by("id")
    
    context={
        'picked_data':picked_data,
        
    }

    return render(request, "durbar_hub_panel/picked_list.html",context)  
            

def hub_picking_from_rider(request,rider_id):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    picked_data = models.RiderOrder.objects.filter(rider_id__rider_id = rider_id,picked = True).order_by("id")
    
    context={
        'picked_data':picked_data,
        
    }

    return render(request, "durbar_hub_panel/hub_collect_order.html",context)  
            
            

def pick_ajax(request):
    if request.is_ajax():
        order_id = request.GET.get("order_id")
        print(order_id)
        models.MerchantOrder.objects.filter(order_id = order_id).update(
            order_track = 4,
            pickup_hub = request.session['h_id'],
            hub_receve_from_rider_time = datetime.datetime.now()
        )
        models.RiderOrder.objects.filter(order_info__order_id=order_id).update(
            submit_to_hub = True,
            picked = False,
            hub_receve_time = datetime.datetime.now()
        )
        data = 'succsess'
        return JsonResponse(data, safe = False)  
        
 


def hub_collection_list(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    collection = models.MerchantOrder.objects.filter(pickup_hub_id = request.session['h_id'],order_track=4).order_by("id")
    
    context={
        'collection':collection,
        
    }

    return render(request, "durbar_hub_panel/order_collection_list.html",context)  
                 


def hub_collection_update(request, order_id):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    data = models.MerchantOrder.objects.filter(order_id = order_id).first()
    if request.method=="POST":
        weight         = int(request.POST[('weight')])
        delivered_hub  = int(request.POST[('delivered_hub')])
        
        models.MerchantOrder.objects.filter(order_id = order_id).update(
            delivered_hub_id = delivered_hub,
            order_track = 5,
            in_transit_time = datetime.datetime.now()
        )
        return redirect("/"+"invoice-print/"+str(order_id)+'/')
    context={
        'data':data,
        
    }

    return render(request, "durbar_hub_panel/collection_update.html",context)  
                 

def sent_to_hub(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    data = models.MerchantOrder.objects.filter(pickup_hub = request.session['h_id'], order_track = 5)
    
    context={
        'data':data,
        
    }

    return render(request, "durbar_hub_panel/sent_to_hub.html",context)  
                 

def in_transit(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    data = models.MerchantOrder.objects.filter(delivered_hub = request.session['h_id'], order_track = 5)
    if request.method=="POST":
        order_id         = request.POST[('order_id')]

        models.MerchantOrder.objects.filter(order_id = order_id).update(
            order_track = 6,
            hub_receve_from_hub_time = datetime.datetime.now()
        )
        return redirect("/in-transit")
    context={
        'data':data,
        
    }

    return render(request, "durbar_hub_panel/in_transit.html",context)  
                 


def collected_for_delevery(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    data = models.MerchantOrder.objects.filter(delivered_hub = request.session['h_id'], order_track = 6)
    rider = models.RiderInfo.objects.filter(hub_id__hub_id = request.session['hub_id']).all()
    
    if request.method=="POST":
        rider         = int(request.POST[('rider')])
        order_id      = int(request.POST[('order_id')])
        collection_amount      = request.POST.get('collection_amount')

        models.RiderDeliveryOrder.objects.create(
            order_info_id = order_id,
            rider_id = rider,
            collection_amount = collection_amount,
            hub_delivery_rider_assign_time = datetime.datetime.now(),

            )
        models.MerchantOrder.objects.filter(id = order_id).update(
            delivered_rider_id = rider,
            hub_rider_assign_for_delivery_time = datetime.datetime.now(),
            order_track = 7
            )
        return redirect("/collected-for-delevery")
    
    context={
        'data':data,
        'rider':rider,
        
    }

    return render(request, "durbar_hub_panel/collected_for_delevery.html",context)  
                 

def Rider_collect_for_delivery(request):
    if request.session.get('hub_id') == False:
        return redirect("/hub")
    data = models.MerchantOrder.objects.filter(delivered_hub = request.session['h_id'], order_track = 7)
    
    context={
        'data':data,
        
        
    }

    return render(request, "durbar_hub_panel/rider_collect_for_delivery.html",context)  
                 


############################### Rider view Start #################################



def rider_login(request):
    if request.method=="POST":
        contact_no1     = request.POST['contact_no1']
        password  = request.POST['password']

        user        = models.RiderInfo.objects.filter(contact_no1 = contact_no1, password = password,status=True).first()
        if user:
            request.session['contact_no1'] = user.contact_no1
            request.session['rider_id'] = user.rider_id
            request.session['r_id'] = user.id
            return redirect("/rider-dashboard/")
        else:
            messages.warning(request, "Wrong Information")
    return render(request, "durbar_rider_panel/rider_login.html")  
            
 
def rider_logout(request):
    request.session['rider_id'] = False
    return redirect('/rider')



def rider_dashboard(request):
    if request.session.get('rider_id') == False:
        return redirect("/rider")
    
    return render(request, "durbar_rider_panel/index.html")  



def rider_pickup_dashboard(request):
    if request.session.get('rider_id') == False:
        return redirect("/rider")
    
    return render(request, "durbar_rider_panel/pickup_index.html")  



def rider_pending_list(request):
    if request.session.get('rider_id') == False:
        return redirect("/rider")
    
    pending_data = models.RiderOrder.objects.filter(rider_id__rider_id = request.session['rider_id'], pending=True).order_by("id")
    
    context={
        'pending_data':pending_data,
        
    }

    return render(request, "durbar_rider_panel/pickup.html",context)  




def rider_picking_order(request,id):
    if request.session.get('rider_id') == False:
        return redirect("/rider")
    
    pending_data = models.RiderOrder.objects.filter(pickup_location_id = id, pending=True).order_by("id")
    
    context={
        'pending_data':pending_data,
        
    }

    return render(request, "durbar_rider_panel/picking.html",context)  


def rider_picking_hold_order(request,id):
    if request.session.get('rider_id') == False:
        return redirect("/rider")
    
    pending_data = models.RiderOrder.objects.filter(pickup_location_id = id, hold=True).order_by("id")
    
    context={
        'pending_data':pending_data,
        
    }

    return render(request, "durbar_rider_panel/hold_picking.html",context)  


def rider_order_collected(request, pickup_location, order_id):
    
    models.MerchantOrder.objects.filter(order_id = order_id).update(
        order_track = 3,
        pickup_rider = request.session['r_id'],
        picked_time = datetime.datetime.now(),
    )
    models.RiderOrder.objects.filter(order_info_id__order_id = order_id).update(
        pending = False,
        hold = False,
        picked = True,
        picked_time = datetime.datetime.now(),
    )
    return redirect('/rider-picking-list/'+str(pickup_location)+'/')
    

def rider_order_cancel(request, pickup_location):
    data = models.RiderOrder.objects.filter(pickup_location_id = pickup_location)
    for i in data:
        models.MerchantOrder.objects.filter(order_id = i.order_info.order_id).update(
        order_track = '21',
        order_picked_by = request.session['r_id'],
        )
        models.RiderOrder.objects.filter(order_info_id__order_id = i.order_info.order_id).delete()

    return redirect('/rider-pending-list')
    
    
    

def rider_merchant_absent(request, pickup_location):
    data = models.RiderOrder.objects.filter(pickup_location_id = pickup_location)
    for i in data:
        models.MerchantOrder.objects.filter(order_id = i.order_info.order_id).update(
        order_track = '22',
        order_picked_by = request.session['r_id'],
        )
        models.RiderOrder.objects.filter(order_info_id__order_id = i.order_info.order_id).delete()

    return redirect('/rider-pending-list')
    
    
    

def rider_order_hold(request, pickup_location, order_id):
    
    models.MerchantOrder.objects.filter(order_id = order_id).update(
        order_track = '19',
        order_picked_by = request.session['r_id'],
        
    )
    models.RiderOrder.objects.filter(order_info_id__order_id = order_id).update(
        pending = False,
        hold = True,
        hold_time = datetime.datetime.now(),
    )
    return redirect('/rider-picking-list/'+str(pickup_location)+'/')
    
    

def rider_hold_list(request):
    if request.session.get('rider_id') == False:
        return redirect("/rider")
    
    hold_data = models.RiderOrder.objects.filter(rider_id__rider_id = request.session['rider_id'], hold=True).order_by("id")
    
    context={
        'hold_data':hold_data,
        
    }

    return render(request, "durbar_rider_panel/hold_list.html",context)  




def rider_order_absent(request, pickup_location, order_id):
    
    models.MerchantOrder.objects.filter(order_id = order_id).update(
        order_track = 20,
        order_picked_by = request.session['r_id'],
        order_absent_time = datetime.datetime.now(),
    )
    models.RiderOrder.objects.filter(order_info_id__order_id = order_id).delete()
    return redirect('/rider-picking-list/'+str(pickup_location)+'/')
    
    
    

def rider_picked_list(request):
    order_list = models.RiderOrder.objects.filter(picked=True)
    context={
        'order_list':order_list,
    }
    return render(request, "durbar_rider_panel/picked.html",context)
    
    
    
    
    

def rider_submited_hub_list(request):
    order_list = models.RiderOrder.objects.filter(submit_to_hub=True)
    context={
        'order_list':order_list,
    }
    return render(request, "durbar_rider_panel/submited_to_hub.html",context)
    
    
    
    
    



