from django.shortcuts import render 
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from datetime import date

from setup.models import Charge 
from mla.models import  TransactionAssessment 

today = date.today()
expirationdate_1year = today + relativedelta(years=1)
expirationdate_6months = today + relativedelta(months=6)

def revalid_tm(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj): 

	try:

# Tricycle
		if engine_size == "Tricycle":

#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 
 


			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months, transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Vehicle License [Tricycle]]
			charge_vehicle_license_tricycle =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Vehicle License Tricycle' )

			particulars = "Vehicle License [Tricycle]";
			amount = charge_vehicle_license_tricycle.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Hackney permit' )

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Driver Badge' )

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




# Motocycle 
		elif engine_size == "Motocycle":

#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 





			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Vehicle License [Motocycle]]
			charge_vehicle_license_motocycle =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Vehicle License Motorcycle' )

			particulars = "Vehicle License [Motocycle]";
			amount = charge_vehicle_license_motocycle .amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', ptaff = staff_obj) 




			#Get particulars [Hackney permit]
			charge_hackney_permit=  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Hackney permit' )

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,   transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Driver Badge' )

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date  = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




		#Get particulars [SMS Alert]
		charge_sms_alert =  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='SMS Alert' )

		particulars = "SMS Alert";
		amount = charge_sms_alert.amount

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 



		#Get particulars [Stamp Duty]
		charge_stamp_duty=  Charge.objects.get(options ='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Stamp Duty' )

		particulars = "Stamp Duty";
		amount = charge_stamp_duty.amount

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin =tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 

		 
		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"