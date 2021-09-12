from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.homepage),
    path('merchant-login/', views.merchant_login),
    path('merchant-register/', views.merchant_register),
    path('bindupozilla/', views.bind_upozilla),  
 



    path('merchant-dashboard/', views.merchant_dashboard),
    path('merchant-logout/', views.merchant_logout), 

    

]
