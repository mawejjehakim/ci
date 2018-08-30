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
 
		
# GENERATE BILL

def bill_dtm(tin_obj, engine_size, cost_price, chassis_number, staff_obj):
 	
		
# GENERATE BILL
	try:
	
	#Get particulars [Registration Fee]
		charge_registration_fee = Charge.objects.get(options='New',  vehicle_type='Dealers Tricycle/Motocycle',  particulars='Registration Fee' )
			
		particulars = "Registration Fee";
		amount =charge_registration_fee.amount

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, expiration_date =expirationdate_1year, amount = amount,  transaction_type = "New Vehicle Registration",  staff = staff_obj)


		#Get particulars [SMS Alert]
		charge_sms_alert = Charge.objects.get(options='New',  vehicle_type='Dealers Tricycle/Motocycle',  particulars='SMS Alert' )
			
		particulars = "SMS Alert";
		amount = charge_sms_alert.amount

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration",  staff = staff_obj)



		#Get particulars [Stamp Duty]
		charge_stamp_duty = Charge.objects.get(options ='New',  vehicle_type='Dealers Tricycle/Motocycle',  particulars='Stamp Duty' )
			
		particulars = "Stamp Duty";
		amount =charge_stamp_duty.amount

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration",  staff = staff_obj)

		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"
	
	 

