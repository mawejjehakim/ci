
from django.urls import path
from django.urls import include

from . import views

urlpatterns = [
   
   	 
   	path('companies/', views.companies, name = "companies" ),
    path('add-company/', views.add_company, name = "add_company" ),
    path('save-company/', views.save_company, name = "save_company" ),
    path('company-preview/', views.company_record_preview, name = "c_data_preview_before_saving" ),

   	path('individuals/', views.individuals, name = "individuals" ),
    path('add-individual/', views.add_individual, name = "add_individual" ),
    path('save-individual/', views.save_individual, name = "save_individual" ),
   	path('individual-preview/', views.individaul_record_preview, name = "i_data_preview_before_saving" ),

    path('edit-individual/<individual_id>/', views.edit_individual, name = "edit_individual" ),
    path('update-individual/', views.update_individual, name = "update_individual" ),

    path('edit-company/<company_id>/', views.edit_company, name = "edit_company" ),
    path('update-company/', views.update_company, name = "update_company" ),


   
    path('save_pic/', views.save_snap, name = 'save_snap') 
    
   	
   	]