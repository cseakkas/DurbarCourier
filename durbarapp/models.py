from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe 
import os

#################### Merchant Panel model  ##########################
 
class Service(models.Model):
    service_title     = models.CharField(max_length=100)
    service_icon     = models.CharField(max_length=50, blank=True)
    service_details   = RichTextField(blank=True)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.service_title
    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
 
class WhyBest(models.Model):
    cause     = models.CharField(max_length=100)
    icon     = models.CharField(max_length=50, blank=True)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.cause
    class Meta:
        verbose_name = 'Why we are the best'
        verbose_name_plural = 'Why we are the best'
 
class DeliveryChargeLocation(models.Model):
    location     = models.CharField(max_length=100)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.location
    class Meta:
        verbose_name = 'Delivery Charge Location'
        verbose_name_plural = 'Delivery Charge Location'
 
class DeliveryChargeWeight(models.Model):
    weight     = models.CharField(max_length=20)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.weight
    class Meta:
        verbose_name = 'Delivery Charge Weight Category'
        verbose_name_plural = 'Delivery Charge Weight Category'
 
 
class ReturnCharge(models.Model):
    charge     = models.CharField(max_length=20)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.charge
    class Meta:
        verbose_name = 'Return Charge'
        verbose_name_plural = 'Return Charge'
 
 
class CollectionCharge(models.Model):
    charge     = models.CharField(max_length=20)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.charge
    class Meta:
        verbose_name = 'Collection Charge'
        verbose_name_plural = 'Collection Charge'
 

 
class CourierProfile(models.Model):
    courier_name     = models.CharField(max_length=100, blank=True)
    slugan       = models.CharField(max_length=100, blank=True)
    page_title   = models.CharField(max_length=100, blank=True)
    email1       = models.EmailField(max_length=100, blank=True)
    email2       = models.EmailField(max_length=100, blank=True)
    mobile1      = models.CharField(max_length=15,  blank=True)
    mobile2      = models.CharField(max_length=15,  blank=True)
    address      = models.TextField(blank=True)
    pro_details  = models.TextField(blank=True)
    logo           = models.ImageField(upload_to='images/logo')
    favicon_logo   = models.ImageField(upload_to='images/logo')
    about_content  = models.TextField(blank=True)
    about_images   = models.ImageField(upload_to='images/about_images')
    why_buy        = models.TextField(blank=True)
    map_locationo  = models.TextField(blank=True)
    facebook_link  = models.TextField(blank=True)
    instagram_link  = models.TextField(blank=True)
    youtube_link  = models.TextField(blank=True)
    linkedin_link  = models.TextField(blank=True)
    staring_year  = models.IntegerField()
    copy_right    = models.CharField(max_length=50, blank=True)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.courier_name
    class Meta:
        verbose_name = 'courier Profile'
        verbose_name_plural = 'courier Profile Information'

class SliderInfo(models.Model):
    slider_name   = models.CharField(max_length=100, blank=True)
    title1        = models.CharField(max_length=200, blank=True)
    title2        = models.CharField(max_length=200, blank=True)
    slider_images = models.ImageField(upload_to='images/slider')
    slider_link   = models.TextField(blank=True)
    upload_date   = models.DateTimeField(auto_now_add=True)
    slider_order  = models.IntegerField()
    status        = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Slider Image'
        verbose_name_plural = 'Slider Images'

    # def url(self):
    #     return os.path.join('/static/durbar_courier/media/images/slider/', os.path.basename(str(self.slider_images)))

    # def photo(self):
    #     return mark_safe('<img src = "{}" width="80"/>'.format(self.url()))

    def __str__(self):
        return self.slider_name




class CollectionPointEntry(models.Model):
    collection_point_name_bangla  = models.CharField(max_length=230)
    collection_point_name_english  = models.CharField(max_length=230)
    ordering       = models.IntegerField(default=0)
    add_date    = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.collection_point_name_bangla)


class PackegeType(models.Model):
    packege_name  = models.CharField(max_length=230)
    ordering       = models.IntegerField(default=0)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.packege_name)


class Collection_time_category(models.Model):
    time  = models.CharField(max_length=230)
    ordering       = models.IntegerField(default=0)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.time)


 
class DeliveryCharge(models.Model):
    delivery_charge_location  = models.ForeignKey(DeliveryChargeLocation, on_delete=models.CASCADE,blank=True,null=True)
    collection_point  = models.ForeignKey(CollectionPointEntry, on_delete=models.CASCADE,blank=True,null=True)
    delivery_charge_weight  = models.ForeignKey(DeliveryChargeWeight, on_delete=models.CASCADE,blank=True,null=True)
    cost     = models.IntegerField(default=0)
    COD_persent     = models.CharField(max_length=20,blank=True,null=True)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return str(self.delivery_charge_location)
    class Meta:
        verbose_name = 'Delivery Charge'
        verbose_name_plural = 'Delivery Charge'


class DistrictEntry(models.Model):
    district_name_bangla  = models.CharField(max_length=230)
    district_name_english  = models.CharField(max_length=230)
    ordering       = models.IntegerField(default=0)
    add_date    = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.district_name_bangla)

class UpazillaEntry(models.Model):
    district_name  = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE)
    upazilla_name_bangla   = models.CharField(max_length=230)
    upazilla_name_english  = models.CharField(max_length=230)
    add_date       = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.upazilla_name_bangla)

class UnionEntry(models.Model):
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE)
    union_name_bangla   = models.CharField(max_length=230)
    union_name_english  = models.CharField(max_length=230)
    add_date       = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.union_name_bangla)

class PostOfficeInfo(models.Model):
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE)
    post_office_bangla    = models.CharField(max_length=230)
    post_office_english    = models.CharField(max_length=230)
    post_code      = models.CharField(max_length=230)
    add_date       = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.post_office_bangla)

class MobileBnakingCategory(models.Model):
    bank_name    = models.CharField(max_length=230)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.bank_name)


class HubInfo(models.Model):
    district_name           = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name           = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    hub_id                        = models.CharField(max_length=50)
    hub_owner_name        = models.CharField(max_length=50)
    address             = models.TextField(null=True,blank=True)
    email                    = models.EmailField( max_length=50,null=True,blank=True)
    password            = models.CharField(max_length=50)
    contact_no1         = models.CharField(unique=True, max_length=50)
    contact_no2         = models.CharField(max_length=50,null=True,blank=True)
    logo                = models.ImageField(upload_to='images/merchant_logo',null=True,blank=True)
    bank_name           = models.CharField(max_length=250,null=True,blank=True)
    bank_ac_no          = models.CharField(max_length=250,null=True,blank=True)
    bank_branch_name    = models.CharField(max_length=250,null=True,blank=True)
    mobile_banking_no   = models.CharField(max_length=250,null=True,blank=True)
    mobile_banking_category = models.ForeignKey(MobileBnakingCategory, on_delete=models.CASCADE,null=True,blank=True)
    trade_license_no    = models.CharField(max_length=250,null=True,blank=True)

    ordering       = models.IntegerField(default=0)
    modifed_by       = models.IntegerField(default=0)
    created_by      = models.IntegerField(default=0)
    created    = models.DateTimeField(auto_now_add = True)
    modify    = models.DateTimeField(auto_now_add = True)
    deleted         = models.BooleanField(default=False)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.hub_id)


class RiderInfo(models.Model):
    district_name           = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name           = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    rider_id                        = models.CharField(max_length=50)
    hub_owner_name        = models.CharField(max_length=50)
    present_address         = models.TextField(null=True,blank=True)
    permanent_address         = models.TextField(null=True,blank=True)
    email                    = models.EmailField(unique=True, max_length=50,null=True,blank=True)
    password            = models.CharField(max_length=50)
    contact_no1         = models.CharField(max_length=50)
    contact_no2         = models.CharField(max_length=50,null=True,blank=True)
    logo                = models.ImageField(upload_to='images/merchant_logo',null=True,blank=True)
    bank_name           = models.CharField(max_length=250,null=True,blank=True)
    bank_ac_no          = models.CharField(max_length=250,null=True,blank=True)
    bank_branch_name    = models.CharField(max_length=250,null=True,blank=True)
    mobile_banking_no   = models.CharField(max_length=250,null=True,blank=True)
    referral_name    = models.CharField(max_length=250,null=True,blank=True)
    referral_phone_no    = models.CharField(max_length=250,null=True,blank=True)
    referral_NID    = models.CharField(max_length=250,null=True,blank=True)
    referral_relation    = models.CharField(max_length=250,null=True,blank=True)

    ordering       = models.IntegerField(default=0)
    modifed_by       = models.IntegerField(default=0)
    created_by      = models.IntegerField(default=0)
    created    = models.DateTimeField(auto_now_add = True)
    modify    = models.DateTimeField(auto_now_add = True)
    deleted         = models.BooleanField(default=False)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.rider_id)


class MerchantInfo(models.Model):
    district_name  = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    marchant_name        = models.CharField(max_length=50)
    address         = models.TextField(null=True,blank=True)
    email        = models.EmailField(unique=True, max_length=50,null=True,blank=True)
    password        = models.CharField(max_length=50)
    contact_no1  = models.CharField(max_length=50)
    contact_no2  = models.CharField(max_length=50,null=True,blank=True)
    logo         = models.ImageField(upload_to='images/merchant_logo',null=True,blank=True)
    ordering       = models.IntegerField(default=0)
    modifed_by       = models.IntegerField(default=0)
    created_by      = models.IntegerField(default=0)
    created    = models.DateTimeField(auto_now_add = True)
    modify    = models.DateTimeField(auto_now_add = True)
    deleted         = models.BooleanField(default=False)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.marchant_name)

class MerchantOrder(models.Model):
    merchant_info                   = models.ForeignKey(MerchantInfo, on_delete=models.CASCADE,null=True)
    district_name                   = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name                   = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    post_office_name                = models.ForeignKey(PostOfficeInfo, on_delete=models.CASCADE,null=True,blank=True)
    order_id                        = models.CharField(max_length=50)
    customer_name                   = models.CharField(max_length=50,null=True,blank=True)
    address                         = models.TextField()
    contact_no1                     = models.CharField(max_length=50,null=True,blank=True)
    contact_no2                     = models.CharField(max_length=50,null=True,blank=True)
    reference_no                    = models.CharField(max_length=50,null=True,blank=True)
    actual_package_price            = models.IntegerField(default=0)
    collection_point                = models.ForeignKey(CollectionPointEntry, on_delete=models.CASCADE,null=True,blank=True)
    packegeType                     = models.ForeignKey(PackegeType, on_delete=models.CASCADE,null=True,blank=True)
    collection_time_category        = models.ForeignKey(Collection_time_category, on_delete=models.CASCADE,null=True,blank=True)
    collection_date                 = models.CharField(max_length=50,null=True,blank=True)
    only_delivery                   = models.BooleanField(default=False)
    delivery_and_amount_collection  = models.BooleanField(default=False)
    lequed_or_Fragile               = models.BooleanField(default=False)
    weight                          = models.ForeignKey(DeliveryChargeWeight, on_delete=models.CASCADE,null=True,blank=True)
    addtional_note                  = models.TextField()
    shipment_charge                 = models.CharField(max_length=50,blank=True)
    cod_charge                      = models.CharField(max_length=50,blank=True)
    lequed_or_Fragile_charge        = models.CharField(max_length=50,blank=True)
    total_service_charge            = models.CharField(max_length=50,blank=True)
    collection_amount               = models.CharField(max_length=50,blank=True)

    ordering                        = models.IntegerField(default=0)
    modifed_by                      = models.IntegerField(default=0)
    created_by                      = models.IntegerField(default=0)
    created                         = models.DateTimeField(auto_now_add = True)
    modify                          = models.DateTimeField(auto_now_add = True)
    deleted                         = models.BooleanField(default=False)
    status                          = models.BooleanField(default=True)

    picked_time                     = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    in_transit_time                 = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    delivered_time                  = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hold_time                       = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_pending_time             = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_to_hub_time              = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_to_merchent_time         = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    canceled_time                   = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    
    order_status_choose = (
        ('1', 'order_placed'),
        ('2', 'customer_absent'),
        ('3', 'in_sorting'),
        ('4', 'payment_done'),

    )
    order_status  = models.CharField(max_length=1, choices=order_status_choose,blank=True)
    
    
    order_track_choose = (
        ('1', 'pending'),
        ('2', 'assign_for_pick'),
        ('3', 'picked'),
        ('4', 'hub_collected_for_ware_house'),
        ('5', 'in_transit'),
        ('6', 'hub_collected_for_delevery'),
        ('7', 'assign_for_delevery'),
        ('8', 'shiping'),
        ('9', 'delivered'),
        ('10', 'hold'),
        ('11', 'return_pending'),
        ('12', 'return_to_hub_for_ware_house '),
        ('13', 'hub_returned_to_ware_house'),
        ('14', 'return_to_hub'),
        ('15', 'assign_for_return'),
        ('16', 'picked_for_return'),
        ('17', 'return_to_merchent'),
        ('18', 'canceled'),
        

    )
    order_track  = models.CharField(max_length=1, choices=order_track_choose,blank=True,default = '1')
    
    
    def __str__(self):
        return str(self.order_id)
