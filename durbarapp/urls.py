from django.urls import path
from . import views 

urlpatterns = [ 
    path('', views.homepage),
    path('merchant-login/', views.merchant_login),



    path('merchant-dashboard/', views.merchant_dashboard),




    

]
