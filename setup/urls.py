
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
   
   	
   	path('login/', views.login, name = "login"),

    path('create-password/', views.create_password, name = "login"),
      

   	path('users/', views.users, name = "users" ),

   	path('add-user/', views.add_user, name = "add_user" ),

    path('institution-types/', views.institution_types, name = "institution_types" ),	

    path('institution-categories/', views.institution_categories, name = "institution_categories" ),  

    path('add-institution-category/', views.add_institution_category, name = "add_institution_category" ), 

    path('edit-institution-category/', views.edit_institution_category, name = "edit_institution_category" ),  

    path('edit-institution-type/', views.edit_institution_type, name = "edit_institution_type" ),  

    path('add-institution-type/', views.add_institution_type, name = "add_institution_type" ),      
 
   	path('lgas/', views.lgas, name = "lgas" ),

   	path('add-lga/', views.add_lga, name = "add_lga" ),

   	path('save-state-code/', views.add_state_code, name = "add_state_code" ),

   	path('charges/', views.charges, name = "charges"),

   	path('add-charge/', views.add_charge, name = "add_charge"),

    path('edit-charge/', views.edit_charge, name = "edit_charge"),



    path('toggle-institution-cat-state/', views.toggle_institution_cat_state, name = "toggle_institution_cat_state"),

     path('toggle-institution-type-state/', views.toggle_institution_type_state, name = "toggle_institution_type_state"),

    path('toggle-charge-state/', views.toggle_charge_state, name = "toggle_charge_state"),

    path('toggle-other-charge-state/', views.toggle_other_charge_state, name = "toggle_other_charge_state"),

    path('other-charges/', views.other_charges, name = "other_charges"),

    path('edit-other-charge/', views.edit_other_charge, name = "edit_other_charge"),

    path('add-other-charge/', views.add_other_charge, name = "add_other_charge"),      

   	path('offices/', views.offices, name = "offices" ),

   	path('add-office/', views.add_office, name = "add_office" ), 

    path('edit-office/', views.edit_office, name = "edit_office" ),

    path('edit-user/<user_id>/', views.edit_user, name = "edit_user" ),

    path('edit-user/', views.edit_user_, name = "edit_user_" ),


    path('edit-lga/', views.edit_lga, name = "edit_lga" ), 

    path('toggle-office-state/', views.toggle_office_state, name = "toggle_office_state" ),

     path('toggle-user-state/', views.toggle_user_state, name = "toggle_user_state" ),

    path('notification-viewed/<notification_id>/', views.notification_viewed, name = "notification_viewed" ),

    path('logout/', views.logout, name = "logout" ),




    path('data-backup/', views.data_backup, name = "edit_lga" ),

    path('data-restore/', views.data_restore, name = "edit_lga" ),

    path('media-data-backup/', views.media_data_backup, name = "edit_lga" ),

    path('media-data-restore/', views.media_data_restore, name = "edit_lga" ),

    path('manage-data/', views.data_management, name = "edit_lga" ),



   


   
   	
   	
   	]