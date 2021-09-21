from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.homepage),
    path('merchant-login/', views.merchant_login),
    path('merchant-register/', views.merchant_register),
 



    path('merchant-dashboard/', views.merchant_dashboard),
    path('new-order/', views.new_order),
    path('order-list/', views.order_list),
    path('load-courses/', views.load_courses, name='ajax_load_upazilla'),
    path('load-post/', views.load_post, name='ajax_load_post'),
    path('merchant-logout/', views.merchant_logout), 

    

]
