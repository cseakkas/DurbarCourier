 
from django.contrib import admin
from . import models
 

class ServiceAdmin(admin.ModelAdmin):
    list_display  = ['service_title', 'status']
 
 

class WhyBestAdmin(admin.ModelAdmin):
    list_display  = ['cause', 'status']
 

class CollectionPointEntryAdmin(admin.ModelAdmin):
    list_display  = ['__str__', 'status']
 
 
 

class DeliveryChargeLocationAdmin(admin.ModelAdmin):
    list_display  = ['location', 'status']
 
 

class DeliveryChargeWeightAdmin(admin.ModelAdmin):
    list_display  = ['weight', 'status']
 
 
 
 

class DeliveryChargeAdmin(admin.ModelAdmin):
    list_display  = ['__str__','collection_point','delivery_charge_weight','cost', 'status']
 

class CollectionChargeAdmin(admin.ModelAdmin):
    list_display  = ['__str__','charge', 'status']
 

class ReturnChargeAdmin(admin.ModelAdmin):
    list_display  = ['__str__','charge', 'status']
 
 

class MerchantInfoAdmin(admin.ModelAdmin):
    list_display  = ['marchant_name', 'email']
 
 
class DistrictEntryAdmin(admin.ModelAdmin):
    list_display  = ['district_name_bangla', 'district_name_english', 'ordering', 'status']
 
 
class UpazillaEntryAdmin(admin.ModelAdmin):
    list_display  = ['upazilla_name_bangla', 'status']
 
 
 
class UnionEntryAdmin(admin.ModelAdmin):
    list_display  = ['union_name_bangla', 'status']
 
 
 
class PostOfficeInfoAdmin(admin.ModelAdmin):
    list_display  = ['post_office_bangla', 'status']
 
 
 
 
class MerchantOrderAdmin(admin.ModelAdmin):
    list_display  = ['order_id','customer_name','contact_no1','reference_no','collection_point','collection_date','weight','total_service_charge', 'status']
 
 
     
admin.site.register(models.Service, ServiceAdmin) 
admin.site.register(models.CollectionCharge, CollectionChargeAdmin) 
admin.site.register(models.ReturnCharge, ReturnChargeAdmin) 
admin.site.register(models.WhyBest, WhyBestAdmin) 
admin.site.register(models.CollectionPointEntry, CollectionPointEntryAdmin) 
admin.site.register(models.DeliveryChargeLocation, DeliveryChargeLocationAdmin) 
admin.site.register(models.DeliveryChargeWeight, DeliveryChargeWeightAdmin) 
admin.site.register(models.DeliveryCharge, DeliveryChargeAdmin) 
admin.site.register(models.MerchantInfo, MerchantInfoAdmin) 
admin.site.register(models.DistrictEntry, DistrictEntryAdmin) 
admin.site.register(models.UpazillaEntry, UpazillaEntryAdmin) 
admin.site.register(models.UnionEntry, UnionEntryAdmin) 
admin.site.register(models.PostOfficeInfo, PostOfficeInfoAdmin) 
admin.site.register(models.MerchantOrder, MerchantOrderAdmin) 