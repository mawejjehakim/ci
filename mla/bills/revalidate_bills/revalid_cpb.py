from django.shortcuts import render 
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from datetime import date

from setup.models import Charge 
from mla.models import  TransactionAssessment 


today = date.today()
expirationdate_1year = today + relativedelta(years=1)
expirationdate_6months = today + relativedelta(months=6)

def revalid_cpb(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj):
 

	try:


# GENERATE BILL

	# 1.6 - 2.0   -  Above 1 million
		if engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle above 1 million" :
		 

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Registration Book')

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Proof of ownership')

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Certificate of road worthiness')

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [1.6 - 2.0]]
			charge_vehicle_license_1_2=  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Vehicle License [1.6 - 2.0]')

			particulars = "Vehicle License [1.6 - 2.0]";
			amount = charge_vehicle_license_1_2.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Hackney permit')

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Driver Badge')

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Conductors Badge')

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 


			transaction_assessments = TransactionAssessment.objects.filter(  tin = tin_obj, transaction_code = transaction_code )
			messages.success(req, "succes", extra_tags = "vehicle_revalidated")
			return render(req, 'view_to_change_vehicle_revalidation.html', {"tin_obj":tin_obj, "transaction_code":transaction_code, "transaction_assessments":transaction_assessments})



		# 2.1 - 3.0   -  Above 1 million
		elif engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle above 1 million" :

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Registration Book')

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Proof of ownership')

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Certificate of road worthiness')

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [2.1 - 3.0]]
			charge_vehicle_license_2_3 =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Vehicle License [2.1 - 3.0]')

			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_vehicle_license_2_3.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Hackney permit')

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Driver Badge')

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Conductors Badge')

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 


			transaction_assessments = TransactionAssessment.objects.filter(  tin = tin_obj, transaction_code = transaction_code )
			messages.success(req, "succes", extra_tags = "vehicle_revalidated")
			return render(req, 'view_to_change_vehicle_revalidation.html', {"tin_obj":tin_obj, "transaction_code":transaction_code, "transaction_assessments":transaction_assessments})


		# 3.1 - Above   -  Above 1 million
		elif engine_size == "3.1 - Above" and cost_price =="Price of vehicle above 1 million" :

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Registration Book')

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Proof of ownership')

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 





			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Certificate of road worthiness')

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [3.1 - above]]
			charge_vehicle_license_3above=  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Vehicle License [3.1 - above]')

			particulars = "Vehicle License [3.1 - above]";
			amount = charge_vehicle_license_3above.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Hackney permit')

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Driver Badge')

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Conductors Badge')

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 


			transaction_assessments = TransactionAssessment.objects.filter(  tin = tin_obj, transaction_code = transaction_code )
			messages.success(req, "succes", extra_tags = "vehicle_revalidated")
			return render(req, 'view_to_change_vehicle_revalidation.html', {"tin_obj":tin_obj, "transaction_code":transaction_code, "transaction_assessments":transaction_assessments})



			#=======================================================================================================================================================
			# 1.6 - 2.0   -  Price of vehicle below 1 million
		elif engine_size == "1.6 - 2.0" and cost_price =="Price of vehicle below 1 million" :

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Registration Book')

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Proof of ownership')

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Certificate of road worthiness')

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [1.6 - 2.0]]
			charge_vehicle_license_1_2 =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Vehicle License [1.6 - 2.0]')

			particulars = "Vehicle License [1.6 - 2.0]";
			amount = charge_vehicle_license_1_2.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Hackney permit')

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Driver Badge')

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Conductors Badge')

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 

			transaction_assessments = TransactionAssessment.objects.filter(  tin = tin_obj, transaction_code = transaction_code )
			messages.success(req, "succes", extra_tags = "vehicle_revalidated")
			return render(req, 'view_to_change_vehicle_revalidation.html', {"tin_obj":tin_obj, "transaction_code":transaction_code, "transaction_assessments":transaction_assessments})



		# 2.1 - 3.0   -  Price of vehicle below 1 million
		elif engine_size == "2.1 - 3.0" and cost_price =="Price of vehicle below 1 million" :

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Registration Book')

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Proof of ownership')

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 





			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Certificate of road worthiness')

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [2.1 - 3.0]]
			charge_vehicle_license_2_3 =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Vehicle License [2.1 - 3.0]')

			particulars = "Vehicle License [2.1 - 3.0]";
			amount = charge_vehicle_license_2_3.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Hackney permit')

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Driver Badge')

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Conductors Badge')

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 

			transaction_assessments = TransactionAssessment.objects.filter(  tin = tin_obj, transaction_code = transaction_code )
			messages.success(req, "succes", extra_tags = "vehicle_revalidated")
			return render(req, 'view_to_change_vehicle_revalidation.html', {"tin_obj":tin_obj, "transaction_code":transaction_code, "transaction_assessments":transaction_assessments})




		# 3.1 - Above   -  Price of vehicle below 1 million
		elif engine_size == "3.1 - Above" and cost_price =="Price of vehicle below 1 million" :

			#Get particulars [Registration Book]
			charge_registration_book =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Registration Book')

			particulars = "Registration Book";
			amount = charge_registration_book.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Proof of ownership]
			charge_proof_of_ownership =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Proof of ownership')

			particulars = "Proof of ownership";
			amount = charge_proof_of_ownership.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 




			#Get particulars [Certificate of road worthiness]
			charge_certificate_of_road_worthiness =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Certificate of road worthiness')

			particulars = "Certificate of road worthiness";
			amount = charge_certificate_of_road_worthiness.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_6months,  transaction_type = 'Revalidation', staff =staff_obj) 


			#Get particulars [Vehicle License [3.1 - above]]
			charge_vehicle_license_3above =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Vehicle License [3.1 - above]')

			particulars = "Vehicle License [3.1 - above]";
			amount = charge_vehicle_license_3above.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Hackney permit]
			charge_hackney_permit =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Hackney permit')

			particulars = "Hackney permit";
			amount = charge_hackney_permit.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Driver Badge]
			charge_driver_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Driver Badge')

			particulars = "Driver Badge";
			amount = charge_driver_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Conductors Badge]
			charge_conductor_badge =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Conductors Badge')

			particulars = "Conductors Badge";
			amount = charge_conductor_badge.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount, expiration_date = expirationdate_1year,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [SMS Alert]
			charge_sms_alert =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='SMS Alert')

			particulars = "SMS Alert";
			amount =charge_sms_alert.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 



			#Get particulars [Stamp Duty]
			charge_stamp_duty =  Charge.objects.get(options = 'New', vehicle_type='Commercial Pickup/Bus', particulars='Stamp Duty')

			particulars = "Stamp Duty";
			amount = charge_stamp_duty.amount


			TransactionAssessment.objects.create(transaction_code = transaction_code, tin = tin_obj, chassis_number  = chassis_number, particulars = particulars, amount = amount,  transaction_type = 'Revalidation', staff =staff_obj) 
			
			 

		return transaction_code

	except Charge.DoesNotExist as e:
		 
		return "charge_unavailable"

		
	except Exception as e:
		print(e)
		return "uncaught_exception"
		 