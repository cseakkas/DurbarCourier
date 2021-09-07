from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe 
import os

#################### Merchant Panel model  ##########################
 
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

class PostOfficeInfo(models.Model):
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE)
    post_office_bangla    = models.CharField(max_length=230)
    post_office_english    = models.CharField(max_length=230)
    post_code      = models.CharField(max_length=230)
    add_date       = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=1)

    def __str__(self):
        return str(self.post_office_bangla)


class HubInfo(models.Model):
    district_name  = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE)
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE)
    Hub_name_bangla  = models.CharField(max_length=230)
    Hub_name_english  = models.CharField(max_length=230)
    address         = models.TextField()
    email        = models.EmailField(unique=True, max_length=50)
    password        = models.CharField(max_length=50)
    contact_no1  = models.CharField(max_length=50)
    contact_no2  = models.CharField(max_length=50)
    ordering       = models.IntegerField(default=0)
    add_date    = models.DateTimeField(auto_now_add = True)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.Hub_name_english)


class MerchantInfo(models.Model):
    district_name  = models.ForeignKey(DistrictEntry, on_delete=models.CASCADE,null=True,blank=True)
    upazilla_name  = models.ForeignKey(UpazillaEntry, on_delete=models.CASCADE,null=True,blank=True)
    marchant_name        = models.CharField(max_length=50)
    address         = models.TextField()
    email        = models.EmailField(unique=True, max_length=50)
    password        = models.CharField(max_length=50)
    contact_no1  = models.CharField(max_length=50)
    contact_no2  = models.CharField(max_length=50)
    logo         = models.ImageField(upload_to='images/merchant_logo')
    ordering       = models.IntegerField(default=0)
    modifed_by       = models.IntegerField(default=0)
    created_by      = models.IntegerField(default=0)
    created    = models.DateTimeField(auto_now_add = True)
    modify    = models.DateTimeField(auto_now_add = True)
    deleted         = models.BooleanField(default=False)
    status         = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.marchant_name)
