 
from django.contrib import admin
from . import models
 

class ServiceAdmin(admin.ModelAdmin):
    list_display  = ['service_title', 'status']
 
 

class WhyBestAdmin(admin.ModelAdmin):
    list_display  = ['cause', 'status']
 

class CollectionPointEntryAdmin(admin.ModelAdmin):
    list_display  = ['__str__', 'status']
 
 
 

 

class DeliveryChargeWeightAdmin(admin.ModelAdmin):
    list_display  = ['weight', 'status']
 
 
 
 

class DeliveryChargeAdmin(admin.ModelAdmin):
    list_display  = ['__str__','delivery_charge_weight','cost', 'status']
 

class CollectionChargeAdmin(admin.ModelAdmin):
    list_display  = ['__str__','charge', 'status']
 

class ReturnChargeAdmin(admin.ModelAdmin):
    list_display  = ['__str__','charge', 'status']
 
 

class MerchantInfoAdmin(admin.ModelAdmin):
    list_display  = ['marchant_name', 'email', 'merchant_id']
 
 
class DistrictEntryAdmin(admin.ModelAdmin):
    list_display  = ['district_name_bangla', 'district_name_english', 'ordering', 'status']
 
 
class UpazillaEntryAdmin(admin.ModelAdmin):
    list_display  = ['upazilla_name_bangla', 'status']
 
 
 
class UnionEntryAdmin(admin.ModelAdmin):
    list_display  = ['union_name_bangla', 'status']
 
 
 
class PostOfficeInfoAdmin(admin.ModelAdmin):
    list_display  = ['post_office_bangla', 'status']
 
 
 
 
class MerchantOrderAdmin(admin.ModelAdmin):
    list_display  = ['order_id','pickup_location','customer_name','contact_no1','reference_no','collection_date','weight','total_service_charge', 'order_track']
 
 
 
class RiderOrderAdmin(admin.ModelAdmin):
    list_display  = ['pickup_location','order_info', 'pending', 'picked', 'submit_to_hub', 'hold', 'order_absent']
 
 
 
 
class PackegeTypeAdmin(admin.ModelAdmin):
    list_display  = ['packege_name', 'status']
 
 
     
admin.site.register(models.Service, ServiceAdmin) 
admin.site.register(models.CollectionCharge, CollectionChargeAdmin) 
admin.site.register(models.ReturnCharge, ReturnChargeAdmin) 
admin.site.register(models.WhyBest, WhyBestAdmin) 
admin.site.register(models.CollectionPointEntry, CollectionPointEntryAdmin) 

admin.site.register(models.DeliveryChargeWeight, DeliveryChargeWeightAdmin) 
admin.site.register(models.MerchantInfo, MerchantInfoAdmin) 
admin.site.register(models.DistrictEntry, DistrictEntryAdmin) 
admin.site.register(models.UpazillaEntry, UpazillaEntryAdmin) 
admin.site.register(models.UnionEntry, UnionEntryAdmin) 
admin.site.register(models.PostOfficeInfo, PostOfficeInfoAdmin) 
admin.site.register(models.MerchantOrder, MerchantOrderAdmin) 
admin.site.register(models.PackegeType, PackegeTypeAdmin) 
admin.site.register(models.Collection_time_category)
admin.site.register(models.DeliveryCharge, DeliveryChargeAdmin) 
admin.site.register(models.HubInfo)
admin.site.register(models.MobileBnakingCategory)
admin.site.register(models.RiderInfo)
admin.site.register(models.PickupLocation)
admin.site.register(models.RiderOrder, RiderOrderAdmin) 
admin.site.register(models.DeliveryCharge_by_Merchant) 
admin.site.register(models.InsideOutsideLocation) 
admin.site.register(models.RiderDeliveryOrder) 
admin.site.register(models.Collection_ammount) 
admin.site.register(models.PaymentStatement) 
admin.site.register(models.ReturnStatement) 