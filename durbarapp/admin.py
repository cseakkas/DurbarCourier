 
from django.contrib import admin
from . import models
 

class MerchantInfoAdmin(admin.ModelAdmin):
    list_display  = ['marchant_name', 'email']
 
 
class DistrictEntryAdmin(admin.ModelAdmin):
    list_display  = ['district_name_bangla', 'district_name_english', 'ordering', 'status']
 
 
class UpazillaEntryAdmin(admin.ModelAdmin):
    list_display  = ['upazilla_name_bangla', 'status']
 
 
 
class PostOfficeInfoAdmin(admin.ModelAdmin):
    list_display  = ['post_office_bangla', 'status']
 
 
     
admin.site.register(models.MerchantInfo, MerchantInfoAdmin) 
admin.site.register(models.DistrictEntry, DistrictEntryAdmin) 
admin.site.register(models.UpazillaEntry, UpazillaEntryAdmin) 
admin.site.register(models.PostOfficeInfo, PostOfficeInfoAdmin) 