from random import randint
from dateutil.relativedelta import relativedelta
from datetime import date

from django.contrib import messages
from django.http import HttpResponseRedirect

from setup.models import Office, User, Charge
from tin.models import  AssignedTin
from mla.models import  TransactionAssessment 

#  pip install python-dateutil install 
range_start = 10**(8-1)
range_end = (10**8)-1
generated_rand_num =  randint(range_start, range_end)
transaction_code = "ML"+str(generated_rand_num)


today = date.today()
expirationdate_1year = today + relativedelta(years=1)
expirationdate_6months = today + relativedelta(month=6)

 
		
# GENERATE BILL

def bill_tm(tin_obj, engine_size, cost_price, chassis_number, staff_obj):
	 		
	# GENERATE BILL

	try:
	# Tricycle
		if (engine_size == "Tricycle"):

		 
			
		 
			#Get particulars [Registration Fee]
			charge_registration_fee = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Registration Fee' )
				
			particulars = "Registration Fee";
			amount = charge_registration_fee.amount 
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
						
					
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='New Plate Number' )
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
						
			
			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_wothiness = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Certificate of road worthiness' )
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_wothiness.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_6months, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
			
			
			#Get particulars [Vehicle License [Tricycle]]
			charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Vehicle License Tricycle' )
				
			particulars = "Vehicle License [Tricycle]";
			amount = charge_vehicle_license.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
			
			
			
					#Get particulars [Hackney permit]
			charge_hacney_permit = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Hackney permit' )
				
			particulars = "Hackney permit";
			amount = charge_hacney_permit.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
			
			
			
			
			#Get particulars [Driver Badge]
			charge_driver_badge = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Driver Badge' )
				
			particulars = "Driver Badge";
			amount = charge_driver_badge.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
			 
		# Motocycle 
		elif engine_size == "Motocycle":

				
			
			#Get particulars [Registration Fee]
			charge_registration_fee = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Registration Fee' )
				
			particulars = "Registration Fee";
			amount = charge_registration_fee.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
						
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='New Plate Number' )
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
						
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_wothiness = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Certificate of road worthiness' )
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_wothiness.amount 

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
					
					
			
			
			#Get particulars [Vehicle License [Motocycle]]
			charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Vehicle License Motorcycle' )
				
			particulars = "Vehicle License [Motocycle]";
			amount = charge_vehicle_license.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
			
			
			
			#Get particulars [Hackney permit]
			charge_hacney_permit = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Hackney permit' )
				
			particulars = "Hackney permit";
			amount = charge_hacney_permit.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
			
			
			
			
			#Get particulars [Driver Badge]
			charge_driver_badge = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Driver Badge' )
				
			particulars = "Driver Badge";
			amount = charge_driver_badge.amount 
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
			
			


	#Get particulars [SMS Alert]
		charge_sms_alert = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='SMS Alert' )
			
		particulars = "SMS Alert";
		amount = charge_sms_alert.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
					
		
		
		#Get particulars [Stamp Duty]
		charge_stamp_duty = Charge.objects.get(options='New', vehicle_type='Commercial Tricycle/Motorcycle', particulars='Stamp Duty' )
			
		particulars = "Stamp Duty";
		amount = charge_stamp_duty.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)

		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"