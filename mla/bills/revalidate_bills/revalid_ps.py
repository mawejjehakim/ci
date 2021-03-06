from django.shortcuts import render 
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from datetime import date

from setup.models import Charge 
from mla.models import  TransactionAssessment 

today = date.today()
expirationdate_1year = today + relativedelta(years=1) 

def revalid_ps(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj): 

	try:
		print(engine_size+"  "+cost_price)


		# GENERATE BILL

		# 1.6 - 2.0   -  Above 1 million
		if engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle above 1 million" :

		#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 

			print("jjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkk")




			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount
			print("0000000000000000000000000")




			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [1.6 - 2.0]]
			charge_vehicle_license1_2 =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [1.6 - 2.0]' )

			particulars = "Vehicle License [1.6 - 2.0]";
			amount = charge_vehicle_license1_2.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 

			print("xxccjjjjjjjjjjjjjjjkkkkkkkkkkkkkkkkkkkk")


			

		# 2.1 - 3.0   -  Above 1 million
		elif engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle above 1 million" :

		#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 






			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [2.1 - 3.0]]
			charge_vehicle_license2_3 =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [2.1 - 3.0]' )

			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_vehicle_license2_3.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


			


		# 3.1 - Above   -  Above 1 million
		elif engine_size == "3.1 - Above" and cost_price =="Price of vehicle above 1 million":

		#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 






			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [3.1 - Above]]
			charge_vehicle_license_3above =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [3.1 - Above]' )

			particulars = "Vehicle License [3.1 - Above]";
			amount = charge_vehicle_license_3above.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


		



		#========================================================================================================================
		# 1.6 - 2.0   -  Price of vehicle below 1 million
		elif engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle below 1 million":

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 






			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [1.6 - 2.0]]
			charge_vehicle_license1_2 =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [1.6 - 2.0]' )

			particulars = "Vehicle License [1.6 - 2.0]";
			amount = charge_vehicle_license1_2.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


		

		# 2.1 - 3.0   -  Price of vehicle below 1 million
		elif engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle below 1 million":
			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 






			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [2.1 - 3.0]]
			charge_vehicle_license2_3 =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [2.1 - 3.0]' )

			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_vehicle_license2_3.amount



			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


		


		# 3.1 - Above   -  Price of vehicle below 1 million
		elif engine_size == "3.1 - Above" and cost_price =="Price of vehicle below 1 million":

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book' )

			particulars = "Registration Book";
			amount = charge_registration_book.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership' )

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness  =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness' )

			particulars = "Certificate of road worthiness";
			amount =charge_certificate_of_road_worthiness .amount

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year, transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [3.1 - Above]]
			charge_vehicle_license_3above =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [3.1 - Above]' )

			particulars = "Vehicle License [3.1 - Above]";
			amount = charge_vehicle_license_3above.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




		print("88888888888888888888888888")
		#Get particulars [SMS Alert]
		charge_sms_alert =  Charge.objects.get(options = 'New', vehicle_type='Private Vehicle Saloon', particulars='SMS Alert' )


		particulars = "SMS Alert";
		amount = charge_sms_alert.amount

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 

		#Get particulars [Stamp Duty]
		charge_stamp_duty =  Charge.objects.get(options ='New', vehicle_type='Private Vehicle Saloon', particulars='Stamp Duty' )

		particulars = "Stamp Duty";
		amount = charge_stamp_duty.amount

		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 

		 
		print(transaction_code)
		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"