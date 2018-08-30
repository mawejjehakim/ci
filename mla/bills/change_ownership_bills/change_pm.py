from random import randint
from dateutil.relativedelta import relativedelta
from datetime import date
from django.contrib import messages
from django.http import HttpResponseRedirect

from setup.models import Office, User, Charge
from tin.models import  AssignedTin
from mla.models import  TransactionAssessment  

today = date.today()
expirationdate_1year = today + relativedelta(years=1)
expirationdate_6months = today + relativedelta(month=6)

 
		
# GENERATE BILL

def change_pm(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj):
	 
	try:
	 
		
# GENERATE BILL


		
			#Get particulars [Registration Fee]
		charge_registration_fee =  Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='Registration Fee')
			
		particulars = "Registration Fee";
		amount = charge_registration_fee.amount 

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
				
		
		
		
		#Get particulars [New Plate Number]
		charge_new_plate_number =  Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='New Plate Number')
			
		particulars = "New Plate Number";
		amount = charge_new_plate_number.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
		
		#Get particulars [Certificate of road worthiness]
		charge_certificate_of_road_worthness =  Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='Certificate of road worthiness')
			
		particulars = "Certificate of road worthiness";
		amount = charge_certificate_of_road_worthness.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
		
		
		#Get particulars [Vehicle License [Motocycle]]
		charge_vehicle_lincense =  Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='Vehicle License Motorcycle')
			
		particulars = "Vehicle License [Motocycle]";
		amount =charge_vehicle_lincense.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
		
		
						#Get particulars [Hackney permit]
		charge_hackney_permit =  Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='Hackney permit')
			
		particulars = "Hackney permit";
		amount = charge_hackney_permit.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
		
		
		
		#Get particulars [Driver Badge]
		charge_driver_badge  = Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='Driver Badge')
			
		particulars = "Driver Badge";
		amount = charge_driver_badge.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
		
		
		
				

	#Get particulars [SMS Alert]
		charge_sms_alert =  Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='SMS Alert')
			
		particulars = "SMS Alert";
		amount = charge_sms_alert.amount 
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
		
		
		#Get particulars [Stamp Duty]
		Charge.objects.get(options='New', vehicle_type='Private Motorcycle', particulars='Stamp Duty')
			
		particulars = "Stamp Duty";
		amount = row['amount'];
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)

		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"