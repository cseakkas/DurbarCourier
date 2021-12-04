from django import template
from django.shortcuts import render, redirect
from django.db.models import Sum, Count, Q
from durbarapp import models
register = template.Library()

@register.filter(name='districtreg')
def District(request):
    name  = models.DistrictEntry.objects.filter(status = True).order_by("-id")
    return name

@register.filter(name='upazillareg')
def Upazilla(request):
    name  = models.UpazillaEntry.objects.filter(status = True).order_by("-id")
    return name


@register.filter(name='weight')
def delivery_weight(request):
    delivery  = models.DeliveryChargeWeight.objects.filter(status = True).order_by("id")
    return delivery


@register.filter(name='point')
def collection_point(request):
    point  = models.CollectionPointEntry.objects.filter(status = True).order_by("-id")
    return point




@register.filter(name='package')
def packagetype(request):
    pack  = models.PackegeType.objects.filter(status = True).order_by("id")
    return pack



@register.filter(name='collection')
def collection_time(request):
    time  = models.Collection_time_category.objects.filter(status = True).order_by("id")
    return time



@register.filter(name='category')
def mobile_banking(request):
    name  = models.MobileBnakingCategory.objects.filter(status = True).order_by("-id")
    return name



@register.filter(name='str2url')
def string_to_url_convert(data):
    #use in view: category = cat.replace('-', ' ')
    # use in html: text|str2url
    data = str(data)    
    return data.replace(' ', '-') 

@register.filter(name='replace')
def replace_load(obj):
    rep = obj.replace("%20"," ")
    return rep
