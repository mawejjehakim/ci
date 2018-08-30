from django.shortcuts import render
from dateutil.relativedelta import relativedelta
from datetime import date
from django.contrib import messages
from django.http import HttpResponseRedirect
from random import randint

from setup.models import Charge 
from mla.models import  TransactionAssessment 
 
today = date.today()
expirationdate_1year = today + relativedelta(years=1)

range_start = 10**(8-1)
range_end = (10**8)-1
generated_rand_num =  randint(range_start, range_end)
transaction_code = "ML"+str(generated_rand_num)


def renew_dv(assessment_type, tin_obj, chassis_number, staff_obj) :

	try:
		 
		 
		#  GENERATE BILL

		# Get particulars Registration Fee
		if assessment_type == "Registration Fee" :
			 
			
			charge_registration_fee  = Charge.objects.get(options = 'Renew', vehicle_type ='Dealers Vehicle', particulars ='Registration Fee')
			 
			particulars = "Registration Fee";
			amount = charge_registration_fee.amount		
			
			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj,  chassis_number = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year , transaction_type = 'Renewal of Particulars', staff = staff_obj)

			
			 
		  
		# Get particulars SMS Alert
		elif assessment_type == "SMS Alert" :
			charge_sms_alert = Charge.objects.get(options = 'Renew', vehicle_type ='Dealers Vehicle', particulars ='SMS Alert' )
			
			particulars = "SMS Alert";
			amount = charge_sms_alert.amount
			
			
			TransactionAssessment.objects.create( transaction_code = transaction_code, tin = tin_obj,  chassis_number = chassis_number, particulars = particulars, amount = amount , transaction_type = 'Renewal of Particulars', staff =staff_obj)
	
			
			
			  

		# Get particulars Stamp Duty
		elif assessment_type == "Stamp Duty" :
			charge_stamp_duty = Charge.objects.get(options = 'Renew', vehicle_type ='Dealers Vehicle', particulars ='Stamp Duty')
			
			particulars = "Stamp Duty";
			amount = charge_stamp_duty.amount

			
			
		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"