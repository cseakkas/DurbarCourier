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
