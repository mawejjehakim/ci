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

def bill_dv(tin_obj, engine_size, cost_price, chassis_number, staff_obj):

	 
	# Get particulars [Registration Fee]

	try:
		charge_registration_fee =  Charge.objects.get(options='New', vehicle_type='Dealers Vehicle', particulars='Registration Fee' )

		particulars = "Registration Fee";
		amount = charge_registration_fee.amount or 0


		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year,  chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)
	

		# Get particulars [SMS Alert]
		charge_sms_alert = Charge.objects.get(options='New', vehicle_type='Dealers Vehicle', particulars='SMS Alert' )
			
		particulars = "SMS Alert";
		amount = charge_sms_alert.amount or 0	
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)		
		
		
		# Get particulars [Stamp Duty]

		charge_stamp_duty = Charge.objects.get(options ='New', vehicle_type='Dealers Vehicle', particulars='Stamp Duty' )
			
		particulars = "Stamp Duty";
		amount = charge_stamp_duty.amount or 0

		# print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx           " + transaction_code)

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj)		

		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"