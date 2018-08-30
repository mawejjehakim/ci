from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from datetime import date
from random import randint

from setup.models import Charge 
from mla.models import  TransactionAssessment 

from django.contrib import messages
from django.http import HttpResponseRedirect

today = date.today()
expirationdate_1year = today + relativedelta(years=1)
expirationdate_6months = today + relativedelta(months=6)

range_start = 10**(8-1)
range_end = (10**8)-1
generated_rand_num =  randint(range_start, range_end)
transaction_code = "ML"+str(generated_rand_num)

def renew_cvs(assessment_type, tin_obj, chassis_number, staff_obj) :

	try:
		
		#Get particulars [Vehicle License [1.6 - 2.0]]
		if assessment_type == "Vehicle License [1.6 - 2.0]" :

			charge_public_vehicle = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , 	particulars='Vehicle License [1.6 - 2.0]' )

			particulars = "Vehicle License [1.6 - 2.0]"

			amount = charge_public_vehicle.amount

			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year, transaction_type = 'Renewal of Particulars', staff =staff_obj) 
			
			


		#Get particulars [Vehicle License [2.1 - 3.0]]
		elif assessment_type == "Vehicle License [2.1 - 3.0]" :
			

		
			charge_vehicle_license_btn2_3 = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , 	particulars='Vehicle License [2.1 - 3.0]' )
			
			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_vehicle_license_btn2_3.amount
			
			
			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year, transaction_type = 'Renewal of Particulars', staff =staff_obj) 		 
			
			
		

		#Get particulars [Vehicle License [3.1 - Above]]				  
		elif assessment_type == "Vehicle License [3.1 - Above]" :
			

		
			charge_vehicle_license_above3 = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars='Vehicle License [3.1 - Above]')

			particulars = "Vehicle License [3.1 - Above]";
			amount = charge_vehicle_license_above3.amount;			

			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year, transaction_type = 'Renewal of Particulars', staff =staff_obj) 		 
			
			

		#Get particulars Certelificate of road worthiness
		elif assessment_type == "Certelificate of road worthiness" :				  
			
		
			charge_certificate_of_road_worthiness= Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' ,particulars='Certelificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months, transaction_type = 'Renewal of Particulars', staff =staff_obj) 					
			
			 			  
				  
			  
			  
			  
		#Get particulars Proof of ownership			  
		elif assessment_type == "Proof of ownership" :
			charge_proof_of_ownership = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars = "Proof of ownership" )
			amount = charge_proof_of_ownership.amount 

			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, transaction_type = 'Renewal of Particulars', staff =staff_obj) 		 
			
			
	  
			  
		#Get particulars New Plate Number				  
		elif assessment_type == "New Plate Number" :
			charge_new_plate_number = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars='New Plate Number' )

			particulars = "New Plate Number"
			amount = charge_new_plate_number.amount


			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, transaction_type = 'Renewal of Particulars', staff =staff_obj) 
			
							  
			  
		#Get particulars Registration Book				  
		elif assessment_type == "Registration Book" :
			charge_registration_book= Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars='Registration Book' )
		
 
			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, transaction_type = 'Renewal of Particulars', staff =staff_obj) 
			
			
  
	
		#Get particulars Driver Badge

		elif assessment_type == "Driver Badge" :
	 
		
			charge_driver_badge = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars='Driver Badge')
		
	 
			particulars = "Driver Badge";
			amount = charge_driver_badge.amount		
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year, transaction_type = 'Renewal of Particulars', staff =staff_obj) 
			
			
			  
		#Get particulars Hackney permit
		elif assessment_type == "Hackney permit" :

		
			charge_hackney_permit = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars='Hackney permit')

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount

			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date  = expirationdate_1year,  transaction_type = 'Renewal of Particulars', staff =staff_obj) 
			
			
			  

		#Get particulars Conductors Badge
		elif assessment_type == "Conductors Badge" :

		
			charge_conductor_badge = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars='Conductors Badge' )
		
			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Renewal of Particulars', staff =staff_obj) 
			
			
			  

		#Get particulars SMS Alert
		elif assessment_type == "SMS Alert" :
			charge_sms_alert = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars='SMS Alert')
		
			particulars = "SMS Alert"
			amount = charge_sms_alert.amount
			
			
			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, transaction_type = 'Renewal of Particulars', staff =staff_obj)
			
			
			  
			  

		#Get particulars Stamp Duty
		elif assessment_type == "Stamp Duty" :
			charge_stamp_duty = Charge.objects.get(options = 'Renew' , vehicle_type='Commercial Vehicle Saloon' , particulars = "Stamp Duty" )
			particulars = "Stamp Duty" 
			amount = charge_stamp_duty.amount

			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, transaction_type = 'Renewal of Particulars', staff =staff_obj) 

			

		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"