from django.core.files.base import File
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe 
import os
from io import BytesIO
from barcode import Code128
from barcode.writer import ImageWriter

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
 
class InsideOutsideLocation(models.Model):
    location     = models.CharField(max_length=100)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return self.location
    class Meta:
        verbose_name = 'Inside Outside Location'
        verbose_name_plural = 'Inside Outside Location'
 
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


 


class DistrictEntry(models.Model):
    district_name_bangla  = models.CharField(max_length=230)
    district_name_english  = models.CharField(max_length=230)
    ordering       = models.IntegerField(default=0)
    is_inside_dhaka    = models.IntegerField(default=0)
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

 
class DeliveryCharge(models.Model): 
    delivery_charge_location  = models.ForeignKey(InsideOutsideLocation, on_delete=models.DO_NOTHING, blank=True,null=True)
    delivery_charge_weight  = models.ForeignKey(DeliveryChargeWeight, on_delete=models.DO_NOTHING, blank=True,null=True)
    cost     = models.IntegerField(default=0)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return str(self.delivery_charge_location)
    class Meta:
        verbose_name = 'Delivery Charge'
        verbose_name_plural = 'Delivery Charge'



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
    owner_image               = models.ImageField(upload_to='images/hub_doc',null=True,blank=True)
    owner_nid_image           = models.ImageField(upload_to='images/hub_doc',null=True,blank=True)
    owner_tin                 = models.ImageField(upload_to='images/hub_doc',null=True,blank=True)
    trade_license             = models.ImageField(upload_to='images/hub_doc',null=True,blank=True)
    bank_name           = models.CharField(max_length=250,null=True,blank=True)
    nid                 = models.CharField(max_length=25,null=True,blank=True)
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
    district_name               = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name                = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    hub                         = models.ForeignKey(HubInfo, on_delete=models.CASCADE,null=True,blank=True)
    rider_id                        = models.CharField(max_length=50)
    rider_name               = models.CharField(max_length=50)
    present_address              = models.TextField(null=True,blank=True)
    permanent_address         = models.TextField(null=True,blank=True)
    email                    = models.EmailField( max_length=50,null=True,blank=True)
    password                         = models.CharField(max_length=50)
    contact_no1         = models.CharField(max_length=50)
    contact_no2         = models.CharField(max_length=50,null=True,blank=True)
    nid                 = models.CharField(max_length=25,null=True,blank=True)
    rider_image               = models.ImageField(upload_to='images/rider_doc',null=True,blank=True)
    rider_nid_image           = models.ImageField(upload_to='images/rider_doc',null=True,blank=True)
    bank_name            = models.CharField(max_length=250,null=True,blank=True)
    bank_ac_no                = models.CharField(max_length=250,null=True,blank=True)
    bank_branch_name      = models.CharField(max_length=250,null=True,blank=True)
    mobile_banking_no         = models.CharField(max_length=250,null=True,blank=True)
    mobile_banking_category = models.ForeignKey(MobileBnakingCategory, on_delete=models.CASCADE,null=True,blank=True)
    referral_name           = models.CharField(max_length=250,null=True,blank=True)
    referral_phone_no    = models.CharField(max_length=250,null=True,blank=True)
    referral_NID         = models.CharField(max_length=250,null=True,blank=True)
    referral_relation    = models.CharField(max_length=250,null=True,blank=True)

    ordering         = models.IntegerField(default=0)
    modifed_by       = models.IntegerField(default=0)
    created_by      = models.IntegerField(default=0)
    created        = models.DateTimeField(auto_now_add = True,null=True,blank=True)
    modify           = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    deleted         = models.BooleanField(default=False)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.rider_id)


class MerchantInfo(models.Model):
    district_name  = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    hub  = models.ForeignKey(HubInfo, on_delete=models.CASCADE,null=True,blank=True)
    marchant_name        = models.CharField(max_length=50)
    merchant_id         = models.CharField(max_length=50,blank=True)
    address         = models.TextField(null=True,blank=True)
    email        = models.EmailField( max_length=50,null=True,blank=True)
    password        = models.CharField(max_length=50)
    contact_no1  = models.CharField(max_length=50)
    contact_no2  = models.CharField(max_length=50,null=True,blank=True)
    bank_name            = models.CharField(max_length=250,null=True,blank=True)
    bank_ac_no                = models.CharField(max_length=250,null=True,blank=True)
    bank_branch_name      = models.CharField(max_length=250,null=True,blank=True)
    mobile_banking_no         = models.CharField(max_length=250,null=True,blank=True)
    mobile_banking_category = models.ForeignKey(MobileBnakingCategory, on_delete=models.CASCADE,null=True,blank=True)
    ordering       = models.IntegerField(default=0)
    modifed_by       = models.IntegerField(default=0)
    created_by      = models.IntegerField(default=0)
    created    = models.DateTimeField(auto_now_add = True)
    modify    = models.DateTimeField(auto_now_add = True)
    deleted         = models.BooleanField(default=False)
    status         = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.merchant_id)


class PickupLocation(models.Model):
    district_name  = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    hub  = models.ForeignKey(HubInfo, on_delete=models.CASCADE,null=True,blank=True)
    merchant  = models.ForeignKey(MerchantInfo, on_delete=models.CASCADE,null=True,blank=True)
    address         = models.TextField(null=True,blank=True)
    contact_no1  = models.CharField(max_length=50)
    contact_no2  = models.CharField(max_length=50,null=True,blank=True)
    ordering       = models.IntegerField(default=0)
    modifed_by       = models.IntegerField(default=0)
    created_by      = models.IntegerField(default=0)
    created    = models.DateTimeField(auto_now_add = True)
    modify    = models.DateTimeField(auto_now_add = True)
    deleted         = models.BooleanField(default=False)
    status         = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.address)

 
class DeliveryCharge_by_Merchant(models.Model):
    merchant         = models.ForeignKey(MerchantInfo, on_delete=models.DO_NOTHING,blank=True,null=True)
    delivery_charge_location  = models.ForeignKey(InsideOutsideLocation, on_delete=models.DO_NOTHING, blank=True,null=True)
    delivery_charge_weight  = models.ForeignKey(DeliveryChargeWeight, on_delete=models.DO_NOTHING,blank=True,null=True)
    cost     = models.IntegerField(default=0)
    status       = models.BooleanField(default=True)

    def __str__(self):
        return str(self.merchant)
    class Meta:
        verbose_name = 'Delivery Charge By Merchant'
        verbose_name_plural = 'Delivery Charge By Merchant'


class MerchantOrder(models.Model):
    merchant_info                   = models.ForeignKey(MerchantInfo, on_delete=models.CASCADE,null=True)
    pickup_rider                    = models.ForeignKey(RiderInfo, on_delete=models.CASCADE, related_name='pickup_rider', null=True,blank=True)
    delivered_rider                 = models.ForeignKey(RiderInfo, on_delete=models.CASCADE, related_name='delivered_rider', null=True,blank=True)
    pickup_hub                      = models.ForeignKey(HubInfo, on_delete=models.CASCADE, related_name='pickup_hub',null=True,blank=True)
    delivered_hub                   = models.ForeignKey(HubInfo, on_delete=models.CASCADE, related_name='delivered_hub', null=True,blank=True)
    district_name                   = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name                   = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    post_office_name                = models.ForeignKey(PostOfficeInfo, on_delete=models.DO_NOTHING,null=True,blank=True)
    order_id                        = models.CharField(max_length=50)
    bar_code                        = models.ImageField(upload_to='images/barcode',null=True,blank=True)
    pickup_location                 = models.ForeignKey(PickupLocation, on_delete=models.CASCADE,null=True,blank=True)
    customer_name                   = models.CharField(max_length=50,null=True,blank=True)
    address                         = models.TextField()
    contact_no1                     = models.CharField(max_length=50,null=True,blank=True)
    contact_no2                     = models.CharField(max_length=50,null=True,blank=True)
    reference_no                    = models.CharField(max_length=50,null=True,blank=True)
    actual_package_price            = models.IntegerField(null=True, blank=True)
    packegeType                     = models.CharField(max_length=150,null=True,blank=True)
    collection_time_category        = models.ForeignKey(Collection_time_category, on_delete=models.DO_NOTHING,null=True,blank=True)
    collection_date                 = models.CharField(max_length=50,null=True,blank=True)
    only_delivery                   = models.BooleanField(default=False)
    delivery_and_amount_collection  = models.BooleanField(default=False)
    lequed_or_Fragile               = models.BooleanField(default=False)
    weight                          = models.ForeignKey(DeliveryCharge, on_delete=models.DO_NOTHING,null=True,blank=True)
    weight_by_merchant              = models.ForeignKey(DeliveryCharge_by_Merchant, on_delete=models.DO_NOTHING,null=True,blank=True)
    addtional_note                  = models.TextField(blank=True)
    shipment_charge                 = models.CharField(max_length=50,blank=True)
    cod_charge                      = models.CharField(max_length=50,blank=True)
    lequed_or_Fragile_charge        = models.CharField(max_length=50,blank=True)
    total_service_charge            = models.CharField(max_length=50,blank=True)
    collection_amount               = models.CharField(max_length=50,blank=True)


    ordering                        = models.IntegerField(default=0)
    modifed_by                      = models.IntegerField(default=0)
    created_by                      = models.IntegerField(default=0)
    created                         = models.DateTimeField(auto_now_add = True,null=True,blank=True)
    modify                          = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    deleted                         = models.BooleanField(default=False)
    status                          = models.BooleanField(default=True)

    picked_time                     = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hub_rider_assign_for_pick_time  = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hub_receve_from_rider_time      = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    in_transit_time                 = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hub_receve_from_hub_time        = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hub_rider_assign_for_delivery_time  = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    rider_pick_for_delivery_time    = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    delivered_time                  = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hold_time                       = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_pending_time             = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_to_delivery_hub_time              = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_to_pickup_hub_time              = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    assign_for_return_time              = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    picked_for_return_time              = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_to_merchent_time         = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    canceled_time                   = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    order_absent_time               = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    
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
        ('12', 'return_to_delevery_hub '),
        ('13', 'return_to_picking_hub'),
        ('14', 'assign_for_return'),
        ('15', 'picked_for_return'),
        ('16', 'return_to_merchent'),
        ('17', 'canceled'),
        ('18', 'picking_hold'),
        ('19', 'order_absent'),
        ('20', 'rider_cancel'),
        ('21', 'merchant_absent'),
        

    )
    order_track  = models.CharField(max_length=3, choices=order_track_choose,blank=True,default = '1')   
    
    return_status_choose = (
        ('1', 'Customer_not_connected_phone'),
        ('2', 'Wrong_product'),
        ('3', 'Customer_abbsent_in_address'),
        ('4', 'Customer_not_interested_to_receve'),

    )
    return_status  = models.CharField(max_length=1, choices=return_status_choose,blank=True)


    def __str__(self):
        return str(self.order_id)

    def save(self, *args, **kwargs):
        data = str(self.order_id)
        r = Code128(data, writer=ImageWriter())
        buffer = BytesIO()
        r.write(buffer)
        self.bar_code.save('barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)



class RiderOrder(models.Model):
    order_info                      = models.ForeignKey(MerchantOrder, on_delete=models.CASCADE,null=True)
    rider                           = models.ForeignKey(RiderInfo, on_delete=models.DO_NOTHING,null=True,blank=True)
    pickup_location                 = models.ForeignKey(PickupLocation, on_delete=models.DO_NOTHING,null=True,blank=True)

    ordering                        = models.IntegerField(default=0)
    modifed_by                      = models.IntegerField(default=0)
    created_by                      = models.IntegerField(default=0)
    created                         = models.DateTimeField(auto_now_add = True)
    modify                          = models.DateTimeField(auto_now_add = True)
    deleted                         = models.BooleanField(default=False)
    status                          = models.BooleanField(default=True)

    picked_time                     = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hub_rider_assign_time           = models.DateTimeField(auto_now_add = True,null=True,blank=True)
    hub_receve_time                  = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    canceled_time                   = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hold_time                       = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    
    
    pending                         = models.BooleanField(default=True)
    picked                          = models.BooleanField(default=False)
    submit_to_hub                   = models.BooleanField(default=False)
    hold                            = models.BooleanField(default=False)
    order_absent                    = models.BooleanField(default=False)
    cancel                          = models.BooleanField(default=False)
    
    
    def __str__(self):
        return str(self.pickup_location)



class RiderDeliveryOrder(models.Model):
    order_info                      = models.ForeignKey(MerchantOrder, on_delete=models.CASCADE,null=True)
    rider                           = models.ForeignKey(RiderInfo, on_delete=models.DO_NOTHING,null=True,blank=True)
    collection_amount               = models.CharField(max_length=50,blank=True)
    otp                             = models.CharField(max_length=10,blank=True)
    
    
    ordering                        = models.IntegerField(default=0)
    modifed_by                      = models.IntegerField(default=0)
    created_by                      = models.IntegerField(default=0)
    created                         = models.DateTimeField(auto_now_add = True)
    modify                          = models.DateTimeField(auto_now_add = True)
    deleted                         = models.BooleanField(default=False)
    status                          = models.BooleanField(default=True)

    delivery_time                   = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hub_delivery_rider_assign_time  = models.DateTimeField(auto_now_add = True,null=True,blank=True)
    hub_receve_time                 = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    canceled_time                   = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hold_time                       = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    
    return_pending_time             = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    return_to_hub_time              = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    
    return_cause                    = models.CharField(max_length=200,blank=True)
    
    order_status_choose = (
        ('1', 'Collect'),
        ('2', 'Delivered'),
        ('3', 'collection_submit_to_hub'),
        ('4', 'return'),
        ('5', 'return_to_hub'),

    )
    order_status  = models.CharField(max_length=1, choices=order_status_choose,blank=True,default = '1')

    
    return_status_choose = (
        ('1', 'Customer_not_connected_phone'),
        ('2', 'Wrong_product'),
        ('3', 'Customer_abbsent_in_address'),
        ('4', 'Customer_not_interested_to_receve'),

    )
    return_status  = models.CharField(max_length=1, choices=return_status_choose,blank=True)


    
    def __str__(self):
        return str(self.order_info)



class Collection_ammount(models.Model):
    order_info                      = models.ForeignKey(MerchantOrder, on_delete=models.CASCADE,null=True)
    collect_rider                   = models.ForeignKey(RiderInfo, on_delete=models.DO_NOTHING,null=True,blank=True)
    collect_hub                     = models.ForeignKey(HubInfo, on_delete=models.DO_NOTHING,null=True,blank=True)
    shipment_charge                 = models.CharField(max_length=50,blank=True)
    cod_charge                      = models.CharField(max_length=50,blank=True)
    lequed_or_Fragile_charge        = models.CharField(max_length=50,blank=True)
    total_service_charge            = models.CharField(max_length=50,blank=True)
    collection_amount               = models.CharField(max_length=50,blank=True)
    is_statement                    = models.BooleanField(default=False)    
    statement_no                    = models.CharField(max_length=50,blank=True,null=True)

    ordering                        = models.IntegerField(default=0)
    modifed_by                      = models.IntegerField(default=0)
    created_by                      = models.IntegerField(default=0)
    created                         = models.DateTimeField(auto_now_add = True)
    modify                          = models.DateTimeField(auto_now_add = False)
    deleted                         = models.BooleanField(default=False)
    status                          = models.BooleanField(default=True)

    rider_collection_time           = models.DateTimeField(auto_now_add = True,null=True,blank=True)
    hub_collection_time             = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    hub_statement_time              = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    head_ofice_collect_time         = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    merchant_statement_time         = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    merchant_collection_time        = models.DateTimeField(auto_now_add = False,null=True,blank=True)
    
    
    collection_status = (
        ('1', 'Rider'),
        ('2', 'Hub'),
        ('3', 'Receve_Pending_Head_Office'),
        ('4', 'Head_Office'),
        ('5', 'Merchant'),

    )
    collection_status  = models.CharField(max_length=1, choices=collection_status,blank=True,default = '1')


    
    def __str__(self):
        return str(self.order_info)



class PaymentStatement(models.Model):
    
    hub_info                        = models.ForeignKey(HubInfo, on_delete=models.DO_NOTHING,null=True,blank=True)
    total_collection_amount         = models.CharField(max_length=50,blank=True)
    statement_no                    = models.CharField(max_length=50,blank=True,null=True)
    head_office_pending             = models.BooleanField(default=True)
    head_office_receved             = models.BooleanField(default=False)
    
    ordering                        = models.IntegerField(default=0)
    modifed_by                      = models.IntegerField(default=0)
    created_by                      = models.IntegerField(default=0)
    created                         = models.DateTimeField(auto_now_add = True)
    modify                          = models.DateTimeField(auto_now_add = False,blank=True,null=True)
    deleted                         = models.BooleanField(default=False)
    status                          = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.statement_no)



