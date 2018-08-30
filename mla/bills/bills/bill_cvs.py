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

def bill_cvs(tin_obj, engine_size, cost_price, chassis_number, staff_obj):
	 
	try:


		# 1.6 - 2.0   -  Above 1 million
		if (engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle above 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Price of vehicle above 1 million]
				charge_price_of_vehicle_above_1m = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Price of vehicle above 1 million')
					
				particulars = "Registration for Price of vehicle above 1 million";
				amount = charge_price_of_vehicle_above_1m
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_wothiness  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_wothiness.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_6months, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Vehicle License [1.6 - 2.0]]
				Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Vehicle License [1.6 - 2.0]')
					
				particulars = "Vehicle License [1.6 - 2.0]";
				amount = row['amount'];
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
						#Get particulars [Hackney permit]
				Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Hackney permit')
					
				particulars = "Hackney permit";
				amount = row['amount'];
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
				#Get particulars [Driver Badge]
				charge_driver_badge = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Driver Badge')
					
				particulars = "Driver Badge";
				amount = charge_driver_badge.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
							



		# 2.1 - 3.0   -  Above 1 million
		elif (engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle above 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number = charge_new_plate_number = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Price of vehicle above 1 million]
				charge_price_of_vehicle_above_1m = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Price of vehicle above 1 million')
					
				particulars = "Registration for Price of vehicle above 1 million";
				amount = charge_price_of_vehicle_above_1m
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_wothiness  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_wothiness.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_6months, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Vehicle License [2.1 - 3.0]]
				charge_vehicle_linces = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Vehicle License [2.1 - 3.0]')
					
				particulars = "Vehicle License [2.1 - 3.0]";
				amount = charge_vehicle_linces.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
								#Get particulars [Hackney permit]
				charge_hackney_permit = charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Hackney permit')
					
				particulars = "Hackney permit";
				amount = charge_hackney_permit.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
				#Get particulars [Driver Badge]
				charge_driver_badge = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Driver Badge')
					
				particulars = "Driver Badge";
				amount = charge_driver_badge.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
						



		# 3.1 - Above   -  Above 1 million
		elif (engine_size == "3.1 - Above" and cost_price =="Price of vehicle above 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Price of vehicle above 1 million]
				charge_price_of_vehicle_above_1m = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Price of vehicle above 1 million')
					
				particulars = "Registration for Price of vehicle above 1 million";
				amount = charge_price_of_vehicle_above_1m
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_wothiness = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_wothiness.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_6months, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Vehicle License [3.1 - above]]
				charge_vehicle_linces = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Vehicle License [3.1 - above]')
					
				particulars = "Vehicle License [3.1 - above]";
				amount =charge_vehicle_linces.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
								#Get particulars [Hackney permit]
				charge_hackney_permit = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Hackney permit')
					
				particulars = "Hackney permit";
				amount = charge_hackney_permit.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
				#Get particulars [Driver Badge]
				charge_driver_badge = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Driver Badge')
					
				particulars = "Driver Badge";
				amount = charge_driver_badge.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
						




		#=======================================================================================================================================================
		# 1.6 - 2.0   -  Price of vehicle below 1 million
		elif (engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle below 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Price of vehicle below 1 million]
				charge_price_of_vehicle_below_1m = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Price of vehicle below 1 million')
					
				particulars = "Registration for Price of vehicle below 1 million";
				amount = charge_price_of_vehicle_below_1m.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_wothiness  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_wothiness.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_6months, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Vehicle License [1.6 - 2.0]]
				charge_vehicle_linces=  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Vehicle License [1.6 - 2.0]')
					
				particulars = "Vehicle License [1.6 - 2.0]";
				amount = charge_vehicle_linces.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
								#Get particulars [Hackney permit]
				charge_hackney_permit = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Hackney permit')
					
				particulars = "Hackney permit";
				amount = charge_hackney_permit.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
				#Get particulars [Driver Badge]
				charge_driver_badge = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Driver Badge')
					
				particulars = "Driver Badge";
				amount = charge_driver_badge.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
						



		# 2.1 - 3.0   -  Price of vehicle below 1 million
		elif (engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle below 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Price of vehicle below 1 million]
				charge_price_of_vehicle_below_1m = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Price of vehicle below 1 million')
					
				particulars = "Registration for Price of vehicle below 1 million";
				amount = charge_price_of_vehicle_below_1m.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_wothiness  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_wothiness.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_6months, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Vehicle License [2.1 - 3.0]]
				charge_vehicle_linces = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Vehicle License [2.1 - 3.0]')
					
				particulars = "Vehicle License [2.1 - 3.0]";
				amount = charge_vehicle_linces.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
								#Get particulars [Hackney permit]
				charge_hackney_permit = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Hackney permit')
					
				particulars = "Hackney permit";
				amount = charge_hackney_permit.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
				#Get particulars [Driver Badge]
				charge_driver_badge = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Driver Badge')
					
				particulars = "Driver Badge";
				amount = charge_driver_badge.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
						



		# 3.1 - Above   -  Price of vehicle below 1 million
		elif (engine_size == "3.1 - Above" and cost_price =="Price of vehicle below 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Price of vehicle below 1 million]
				charge_vehicle_below_1m =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Price of vehicle below 1 million')
					
				particulars = "Registration for Price of vehicle below 1 million";
				amount = charge_vehicle_below_1m.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_wothiness  = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_wothiness.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_6months, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				#Get particulars [Vehicle License [3.1 - above]]
				charge_vehicle_license_above_3 =   Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Vehicle License [3.1 - above]')
					
				particulars = "Vehicle License [3.1 - above]";
				amount = charge_vehicle_license_above_3.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
								#Get particulars [Hackney permit]
				charge_hackney_permit = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Hackney permit')
					
				particulars = "Hackney permit";
				amount = charge_hackney_permit.amount_permit.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
				#Get particulars [Driver Badge]
				charge_driver_badge = Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Driver Badge')
					
				particulars = "Driver Badge";
				amount = charge_driver_badge.amount
				
				
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj,  expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
				
				
				
					


	#Get particulars [SMS Alert]
		charge_sms_alert =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='SMS Alert')
				
		particulars = "SMS Alert";
		amount = charge_sms_alert.amount
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
		
			
			
			#Get particulars [Stamp Duty]
		charge_stamp_duty =  Charge.objects.get(options='New',  vehicle_type='Commercial Vehicle Saloon',  particulars='Stamp Duty')
				
		particulars = "Stamp Duty";
		amount = charge_stamp_duty.amount
		
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "New Vehicle Registration", staff = staff_obj )
		
		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"