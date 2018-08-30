
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
   

      path('plate-numbers/', views.number_plates, name = "number_plates" ),

      path('add-number-plate/', views.add_number_plate, name = "add_number_plate" ),

      path('number-plate-preview/', views.number_plate_record_preview, name = "number_plate_record_preview" ),

      path('save-number-plate/', views.save_number_plate, name = "save_number_plate" ),

      path('get-office-plates/', views.get_office_plates, name = "get_office_plates" ),

      path('get-lgov-numberplates/',views.get_lg_number_plates, name = "get_lgov_numberplates"),
      
      path('issue-reissue-car-plate/', views.issue_reissue_number_plate, name="issue_reissue_number_plate"),

      path('check-plate/<plate_number>/', views.check_number_plate, name="check_number_plate"),

      path('edit-number-plate/', views.edit_number_plate, name="edit_number_plate"),

      path('edit-plate-lg/', views.edit_number_plate_lg, name="edit_number_plate_lg"),

   	
   	]
   	

      