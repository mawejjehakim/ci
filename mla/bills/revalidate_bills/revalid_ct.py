from django.shortcuts import render 
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from datetime import date

from setup.models import Charge 
from mla.models import  TransactionAssessment 

today = date.today()
expirationdate_1year = today + relativedelta(years=1)
expirationdate_6months = today + relativedelta(months=6)

def revalid_ct(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj):

	try:

# GENERATE BILL

		# 6 - 8 tyres   -  Above 1 million
		if engine_size == "6 - 8 tyres" :



			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 		

			#Get particulars [Vehicle License [6 - 8 tyres]]
			charge_vehicle_license_6_8tyres =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Vehicle License [6 - 8 tyres]' )

			particulars = "Vehicle License [6 - 8 tyres]";
			amount = charge_vehicle_license_6_8tyres.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 


				#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Hackney permit [6 - 8 tyres]' )

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Driver Badge' )

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



				#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Conductors Badge' )

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 





		# 10 tyres - above 
		elif engine_size == "10 tyres - above" :



			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 





			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount




			#Get particulars [Vehicle License [10 tyres - above]]
			charge_vehicle_license_10_above_tyres =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Vehicle License [10 tyres - above]' )

			particulars = "Vehicle License [10 tyres - above]";
			amount = charge_vehicle_license_10_above_tyres.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 


						#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Hackney permit [10 tyres - above]' )

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Driver Badge' )

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



				#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Conductors Badge' )

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [SMS Alert]
			charge_sms_alert =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='SMS Alert' )

			particulars = "SMS Alert";
			amount = charge_sms_alert.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Stamp Duty]
			charge_stamp_duty =  Charge.objects.get(options = 'New', vehicle_type='Commercial Truck/Trailer/Lorry/Tipper', particulars='Stamp Duty' )

			particulars = "Stamp Duty";
			amount = charge_stamp_duty.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 

			 
		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"
		 