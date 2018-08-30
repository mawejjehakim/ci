
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
 

      path('mdas/', views.mdas, name = "mdas" ),

      path('add-mda/', views.add_mda, name = "add_mda"),

      path('add-revenue-item/', views.add_revenue_item, name = "add_revenue_item"),

      path('revenue-items/', views.revenue_items, name = "revenue_items"),

      path('genearate-bill/', views.get_tin_info_generate_bill, name = "get_tin_info_generate_bill"),
     
      path('make-payment/', views.make_payement, name = "make_payement"),

      path('select-payment/', views.select_payement_without_details, name = "select_payement_without_details"),

      path('select-payment/<tin_number>/<bill_number>/', views.select_payement, name = "select_payement"),

      path('get-bill/', views.get_bill, name = "get_bill"),
 

      
   	
   	]