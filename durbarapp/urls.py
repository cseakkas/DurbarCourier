from django.urls import path
from . import views 

urlpatterns = [ 
############################### website url ###################################

    path('', views.homepage),
 
############################### Merchant url ###################################

    path('merchant-dashboard/', views.merchant_dashboard),
    path('new-order/', views.new_order),
    path('order-list/', views.order_list),
    path('service-charge-list/', views.service_charge_list),
    path('customer-info-edit/', views.customer_info_edit),

    path('load-courses/', views.load_courses, name='ajax_load_upazilla'),
    path('load-post/', views.load_post, name='ajax_load_post'),

    path('load-weight/', views.load_weight, name='ajax_load_weight'),
    path('load-cost/', views.load_cost, name='ajax_load_cost'),

    path('merchant-login/', views.merchant_login), 
    path('merchant-logout/', views.merchant_logout), 

############################### Admin url ###################################
    path('admin-dashboard/', views.admin_dashboard),


    path('all-order/', views.all_order_list),
    path('pending-order/', views.pending_list),
    path('assign_for_pick-order/', views.assign_for_pick_list),
    path('picked-order/', views.picked_list),
    path('hub_collected_for_ware_house-order/', views.hub_collected_for_ware_house_list),
    path('in_transit-order/', views.in_transit_list),
    path('hub_collected_for_delevery-order/', views.hub_collected_for_delevery_list),
    path('assign_for_delevery-order/', views.assign_for_delevery_list),
    path('shiping-order/', views.shiping_list),
    path('delivered-order/', views.delivered_list),
    path('hold-order/', views.hold_list),
    path('return_pending-order/', views.return_pending_list),
    path('return_to_hub_for_ware_house-order/', views.return_to_hub_for_ware_house_list),
    path('hub_returned_to_ware_house-order/', views.hub_returned_to_ware_house_list),
    path('return_to_hub-order/', views.return_to_hub_list),
    path('assign_for_return-order/', views.assign_for_return_list),
    path('picked_for_return-order/', views.picked_for_return_list),
    path('return_to_merchent-order/', views.return_to_merchent_list),
    path('canceled-order/', views.canceled_list),

    path('order-upgrade/<int:id>/', views.order_upgrade),
    path('add-hub/', views.add_hub),
    

]
