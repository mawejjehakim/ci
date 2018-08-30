from random import randint
from dateutil.relativedelta import relativedelta
from datetime import date
from django.shortcuts import render

from django.contrib import messages
from django.http import HttpResponseRedirect

from setup.models import Office, User, Charge
from tin.models import  AssignedTin
from mla.models import  TransactionAssessment  

today = date.today()
expirationdate_1year = today + relativedelta(years=1)

 
		
# GENERATE BILL


def change_ps(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj):
	print("edfg")
	 
	try:				
		# 1.6 - 2.0   -  Above 1 million
		if (engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle above 1 million"):
			

			
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book')
			particulars  =  "Registration Book";
	 
			amount = charge_registration_book.amount 

					

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
			

			#Get particulars [Inspection Fee]
			charge_inspection_fee= Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Inspection Fee' )
			particulars = "Inspection Fee";

			amount  = charge_inspection_fee.amount 		

					
		
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get( options='New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership')
				
			particulars = "Proof of ownership";

			amount  = charge_proof_of_ownership.amount 

					
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='New Plate Number')
				
			particulars = "New Plate Number";


			amount  = charge_new_plate_number.amount 

					
			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
			
			#Get particulars [Price of vehicle above 1 million]
			charge_price_of_vehicle_obove_1m = Charge.objects.get(options='New',  vehicle_type='Private Vehicle Saloon', particulars='Price of vehicle above 1 million')
			
			particulars = "Registration for Price of vehicle above 1 million";

			amount  = charge_price_of_vehicle_obove_1m.amount 

			

			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness = Charge.objects.get(options='New',   vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";

			amount = charge_certificate_of_road_worthiness.amount 

			

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			 
			#Get particulars [Vehicle License [1.6 - 2.0]]
			charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [1.6 - 2.0]')
				
			particulars = "Vehicle License [1.6 - 2.0]";


			amount  = charge_vehicle_license.amount

			
			
			TransactionAssessment.objects.create(transaction_code = transaction_code,  expiration_date = expirationdate_1year, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			 


		# 2.1 - 3.0   -  Above 1 million
		elif (engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle above 1 million"):
			 # here

			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book')
			 	
			particulars = "Registration Book";
			amount = charge_registration_book.amount 

			

			 
			TransactionAssessment.objects.create(transaction_code = transaction_code,  expiration_date = expirationdate_1year, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
			 
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Inspection Fee')
				
			articulars = "Inspection Fee";
			amount = charge_inspection_fee.amount 
			

			

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New',  expiration_date = expirationdate_1year, vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount 
			

			

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount 
			

			

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
			
			
			#Get particulars [Price of vehicle above 1 million]
			charge_price_of_vehicle_obove_1m = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Price of vehicle above 1 million')
				
			particulars = "Registration for Price of vehicle above 1 million";
			
			amount  = charge_price_of_vehicle_obove_1m.amount
			
			
				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness = Charge.objects.get(options='New', expiration_date = expirationdate_1year, vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";

			amount = charge_certificate_of_road_worthiness.amount 

			

						
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Vehicle License [2.1 - 3.0]]
			charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [2.1 - 3.0]')
				
			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_vehicle_license.amount 
				

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			

		# 3.1 - Above   -  Above 1 million
		elif (engine_size == "3.1 - Above" and cost_price =="Price of vehicle above 1 million"):
			
			#Get particulars [Registration Book]
			charge_registration_book = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book')
				
			particulars = "Registration Book";
			amount = charge_registration_book.amount 

						

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Inspection Fee]
			charge_inspection_fee = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Inspection Fee')
				
			particulars = "Inspection Fee";
			amount = charge_inspection_fee.amount 
						

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Proof of ownership]
			charge_proof_of_ownership = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership')
				
			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount 
				

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			
			#Get particulars [New Plate Number]
			charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='New Plate Number')
				
			particulars = "New Plate Number";
			amount = charge_new_plate_number.amount 
			

			

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Price of vehicle above 1 million]
			charge_price_of_vehicle_obove_1m = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Price of vehicle above 1 million')
				
			particulars = "Registration for Price of vehicle above 1 million";
			
			amount  = charge_price_of_vehicle_obove_1m.amount
						
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness')
				
			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount 

			

			

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			
			#Get particulars [Vehicle License [3.1 - above]]
			charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [3.1 - above]')
				
			particulars = "Vehicle License [3.1 - above]";
			amount = charge_vehicle_license.amount 
			

			

				
			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
			



	#=======================================================================================================================================================
	# 1.6 - 2.0   -  Price of vehicle below 1 million
		elif (engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle below 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount 
				

				
					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Price of vehicle below 1 million]
				charge_price_of_vehicle_obove_1m = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Price of vehicle below 1 million')
					
				particulars = "Registration for Price of vehicle below 1 million";
				
				amount  = charge_price_of_vehicle_obove_1m.amount 
				
						
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_road_worthiness = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_road_worthiness.amount 

				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
				
				
				#Get particulars [Vehicle License [1.6 - 2.0]]
				charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [1.6 - 2.0]')
					
				particulars = "Vehicle License [1.6 - 2.0]";
				amount = charge_vehicle_license.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
				
				



		# 2.1 - 3.0   -  Price of vehicle below 1 million
		elif (engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle below 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj)			
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number= Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Price of vehicle below 1 million]
				charge_price_of_vehicle_obove_1m = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Price of vehicle below 1 million')
					
				particulars = "Registration for Price of vehicle below 1 million";
				amount  = charge_price_of_vehicle_obove_1m.amount 
						 
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_road_worthiness = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_road_worthiness.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		        
				
				
				#Get particulars [Vehicle License [2.1 - 3.0]]
				charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [2.1 - 3.0]')
					
				particulars = "Vehicle License [2.1 - 3.0]";
				amount = charge_vehicle_license.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, expiration_date = expirationdate_1year, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		        
				
				



		# 3.1 - Above   -  Price of vehicle below 1 million
		elif (engine_size == "3.1 - Above" and cost_price =="Price of vehicle below 1 million"):
			
				#Get particulars [Registration Book]
				charge_registration_book = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Registration Book')
					
				particulars = "Registration Book";
				amount = charge_registration_book.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Inspection Fee]
				charge_inspection_fee = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Inspection Fee')
					
				particulars = "Inspection Fee";
				amount = charge_inspection_fee.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Proof of ownership]
				charge_proof_of_ownership = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Proof of ownership')
					
				particulars = "Proof of ownership";
				amount = charge_proof_of_ownership.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		        
				
				
				#Get particulars [New Plate Number]
				charge_new_plate_number = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='New Plate Number')
					
				particulars = "New Plate Number";
				amount = charge_new_plate_number.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Price of vehicle below 1 million]
				charge_price_of_vehicle_obove_1m = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Price of vehicle below 1 million')
					
				particulars = "Registration for Price of vehicle below 1 million";
				
				
				amount  = charge_price_of_vehicle_obove_1m.amount 
					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
				
				
				#Get particulars [Certificate of road worthiness]
				charge_certificate_of_road_worthiness = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Certificate of road worthiness')
					
				particulars = "Certificate of road worthiness";
				amount = charge_certificate_of_road_worthiness.amount 
				

				

					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 
				
				
				#Get particulars [Vehicle License [3.1 - above]]
				charge_vehicle_license = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Vehicle License [3.1 - above]')
					
				particulars = "Vehicle License [3.1 - above]";
				amount = charge_vehicle_license.amount 
				
					
				TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		        
				
				




		#Get particulars [SMS Alert]
		charge_sms_alert = Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='SMS Alert')
			
		particulars = "SMS Alert";
		amount  = charge_sms_alert.amount 
		
			
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
		
		
		
		#Get particulars [Stamp Duty]
		charge_stamp_duty= Charge.objects.get(options='New', vehicle_type='Private Vehicle Saloon', particulars='Stamp Duty')
			
		particulars = "Stamp Duty";
		
		amount  = charge_stamp_duty.amount 
		
		TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  =  chassis_number, particulars = particulars, amount = amount,  transaction_type = "Change of ownership",  staff = staff_obj) 		       
		
		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"