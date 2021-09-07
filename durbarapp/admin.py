 
from django.contrib import admin
from . import models
 

class MerchantInfoAdmin(admin.ModelAdmin):
    list_display  = ['marchant_name', 'email']
 
 
     
admin.site.register(models.MerchantInfo, MerchantInfoAdmin) 