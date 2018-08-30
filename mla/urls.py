
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
   
      path('get-tin-info/', views.get_tin_info, name = "get_tin_info" ),

      path('vehicles/', views.vehicles, name = "vehicles" ),

      path('vehicle-preview/', views.vehicle_record_preview, name = "vehicle_record_preview" ),

      path('save-vehicle/',views.save_vehicle, name = "save_vehicle"),

      path('learners/', views.learners, name = "learners" ),

      path('change-vehicle-ownership/', views.change_vehicle_ownership, name = "change_vehicle_ownership" ),

      path('mark-stolen-vehicle/', views.mark_stolen_vehicle, name = "mark_stolen_vehicle" ),

      path('mark-stolen-vehicle/<plate_id>/', views.mark_stolen_vehicle, name = "mark_stolen_vehicle" ),

      path('mark-vehicle/', views.mark_vehicle, name="mark_vehicle"),

      path('get-learners-permit/', views.get_tin_info_learners_permit, name = "get_tin_info_learners_permit" ),

      path('save-learners-permit/', views.save_learners_permit, name="save_learners_permit"),

      path('get-vehicle-revalidation/', views.get_chassisnumber_info_vehicle_revalidation, name="get_chassisnumber_info_vehicle_revalidation"),
# 
      path('save-vehicle-revalidation/', views.save_vehicle_revalidation, name="save_vehicle_revalidation"),

      path('get-for-vehicle-assessment/', views.get_info_vehicle_assessment, name="get_info_vehicle_assessment"),

      path('save-vehicle-assessment/', views.save_vehicle_assessment, name="save_vehicle_assessment"),

      path('save-change-ownership/', views.save_change_of_ownership, name="save_change_of_ownership"),
      

   	
   	
   	]