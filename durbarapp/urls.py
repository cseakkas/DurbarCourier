from django.urls import path
from . import views 
from . import merchant_views 

urlpatterns = [ 
############################### website url ###################################

    path('', views.homepage),
 
############################### Merchant url ###################################

    path('merchant-dashboard/', merchant_views.merchant_dashboard),
    path('new-order/', merchant_views.new_order),
    path('merchant-profile/', merchant_views.merchant_profile),
    path('order-list/', merchant_views.order_list),
    path('service-charge-list/', merchant_views.service_charge_list),
    path('customer-info-edit/', merchant_views.customer_info_edit),

    path('marchant-order-tracking/', merchant_views.marchant_order_tracking),

    path('load-courses/', merchant_views.load_courses, name='ajax_load_upazilla'),
    path('load-post/', merchant_views.load_post, name='ajax_load_post'),
    path('load-hub/', merchant_views.load_hub, name='ajax_load_hub'),

    path('load-weight/', merchant_views.load_weight, name='ajax_load_weight'),
    path('load-cost/', merchant_views.load_cost, name='ajax_load_cost'),

    path('merchant-login/', merchant_views.merchant_login), 
    path('merchant-logout/', merchant_views.merchant_logout), 

############################### Admin url ###################################
    path('update-upazilla/', views.update_upazilla, name='ajax_update_upazilla'),
    path('select-hub/', views.select_hub, name='ajax_select_hub'),
    path('update-hub/', views.update_hub, name='ajax_update_hub'),
    
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
    path('add-rider/', views.add_rider),
    path('hub-list/', views.hub_list),
    path('rider-list/', views.rider_list),
    path('rider/<str:rider_id>/update/', views.rider_update),
    path('merchant-request/', views.merchent_request),
    path('merchant-approval/<int:id>/', views.merchant_approval),
    path('merchant-management/', views.merchant_management_list),
    path('merchant-management/<str:id>/', views.merchant_management_edit),


############################### Hub url ###################################

    path('hub/', views.hub_login),
    path('hub-logout/', views.hub_logout),
    path('hub-dashboard/', views.hub_dashboard),
    path('hub-pending/', views.hub_pending_list),
    path('hub-picked/', views.hub_picking_from_rider_list),
    path('hub-picking/<str:rider_id>/', views.hub_picking_from_rider),
    path('hub-pick/', views.pick_ajax),
    path('hub-pending-update/<str:id>/', views.hub_pending_update),
    path('hub-collection-list/', views.hub_collection_list),
    path('hub-collection-update/<str:order_id>/', views.hub_collection_update),
    path('invoice-print/<str:order_id>/', views.invoice_print),
    path('sent-to-hub/', views.sent_to_hub),
    path('in-transit/', views.in_transit),
    path('collected-for-delevery/', views.collected_for_delevery),
    path('rider-collect-for-delivery/', views.Rider_collect_for_delivery),



############################### Rider url ###################################

    path('rider/', views.rider_login),
    path('rider-logout/', views.rider_logout),
    path('rider-dashboard/', views.rider_dashboard),
    path('rider-pickup-dashboard/', views.rider_pickup_dashboard),
    path('rider-pending-list/', views.rider_pending_list),
    path('rider-cancel-order/<int:pickup_location>/', views.rider_order_cancel),
    path('rider-merchant-absent/<int:pickup_location>/', views.rider_merchant_absent),
    path('rider-hold-list/', views.rider_hold_list),
    path('rider-picking-list/<int:id>/', views.rider_picking_order),
    path('rider-picking-hold-list/<int:id>/', views.rider_picking_hold_order),
    path('rider-collect-order/<int:pickup_location>/<str:order_id>/', views.rider_order_collected),
    path('rider-hold-order/<int:pickup_location>/<str:order_id>/', views.rider_order_hold),
    path('rider-product-absent-order/<int:pickup_location>/<str:order_id>/', views.rider_order_absent),
    path('rider-picked-list/', views.rider_picked_list),
    path('rider-submited-to-hub-list/', views.rider_submited_hub_list),





]
