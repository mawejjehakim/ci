from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q
from pbkdf2 import crypt

from tin.models import AssignedTin, Company, Individual

from setup.models import Office, User, ChargesOthers, Notification

from store.models import NumberPlate

from mla.forms import TinNumberForm, PlateNumberForm, VehicleForm, TINForm, VehicleAssessmentForm, SingleValueCharFieldForm, ChassisNumberFieldForm, PlateWithPassForm,PlateNumberObjForm

from mla.models import  Vehicle, TransactionAssessment, LearnersPermit,  Revalidation

from mla.bills.generate_assessment_bill import generate_assessment_bill
from mla.bills.generate_assessment_bill_change_ownership import generate_assessment_bill_change_ownership

from mla.bills.generate_assessment_bill_vehicle_assessment import generate_assessment_bill_vehicle_assessment

from mla.bills.generate_assessment_bill_revalidation import generate_assessment_bill_vehicle_revalidation




from mla.bills.renew_bills.renew_ps import renew_ps
from mla.bills.renew_bills.renew_dv import renew_dv
from mla.bills.renew_bills.renew_cpb import renew_cpb
from mla.bills.renew_bills.renew_ct import renew_ct
from mla.bills.renew_bills.renew_tm import renew_tm
from mla.bills.renew_bills.renew_cvs import renew_cvs
from mla.bills.renew_bills.renew_dtm import renew_dtm
from mla.bills.renew_bills.renew_pm import renew_pm
from mla.bills.renew_bills.renew_ppb import renew_ppb

from mla.bills.revalidate_bills.revalid_pm import revalid_pm
from mla.bills.revalidate_bills.revalid_tm import revalid_tm
from mla.bills.revalidate_bills.revalid_ppb import revalid_ppb
from mla.bills.revalidate_bills.revalid_cpb import revalid_cpb
from mla.bills.revalidate_bills.revalid_ps import revalid_ps
from mla.bills.revalidate_bills.revalid_cvs import revalid_cvs
from mla.bills.revalidate_bills.revalid_ct import revalid_ct
 



from random import randint
from dateutil.relativedelta import relativedelta
from datetime import date


from django.contrib import messages

today = date.today()
expirationdate_1year = today + relativedelta(years=1)


def t_code():
	range_start = 10**(8-1)
	range_end = (10**8)-1
	generated_rand_num =  randint(range_start, range_end)
	tcode = "ML"+str(generated_rand_num)

	return tcode

def get_tin_info(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA User' or "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_tin_info.html')			

			elif req.method == "POST" and req.POST: 		 
				form = TinNumberForm(req.POST)

				if form.is_valid(): 
					tin_number = form.cleaned_data.get("tin")
					existing_tin =  AssignedTin.objects.filter(tin = tin_number)

					 

					if existing_tin.exists():
						if len(existing_tin) >1: 
							 
							return HttpResponseRedirect('/mla/get-tin-info/')
						else:

							tin_obj =  existing_tin.first()
							vehicle_category = req.POST.get("vehicle_category")
							if tin_obj.tin_for == "Company":
								try:
									company = Company.objects.get(tin = tin_obj.id)
									 
									if vehicle_category ==  "Private Vehicle Saloon" or vehicle_category == "Commercial Vehicle Saloon" or vehicle_category == "Private Pickup/Bus" or vehicle_category == "Commercial Pickup/Bus" or vehicle_category == "Dealers Vehicle":
										engine_size = True
										no_of_tyres = False
										engine_category = False

										
									elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
										no_of_tyres = True
										engine_size = False
										engine_category = False

										

									elif vehicle_category == "Commercial Tricycle/Motorcycle" or vehicle_category == "Private Motorcycle" or vehicle_category == "Dealers Tricycle/Motorcycle":
										engine_category = True
										no_of_tyres = False
										engine_size = False

									tin = company.tin
									local_government = company.local_government
									bussiness_status = company.bussiness_status
									bussiness_class = company.bussiness_class
									registration_number = company.registration_number
									bussiness_name = company.bussiness_name
									bussiness_owner = company.bussiness_owner

									return render(req, 'add_vehicle.html', {'current_owner_tin':tin.tin,'vehicle_category':vehicle_category,   'local_government':local_government, 'bussiness_status':bussiness_status, 'registration_number':registration_number, 'bussiness_name':bussiness_name, 'bussiness_owner':bussiness_owner, "register_for":"company",  "engine_size":engine_size, "no_of_tyres":no_of_tyres, "engine_category":engine_category}) 

								except Company.DoesNotExist:
									 
									messages.info(req, "invalid form fields", extra_tags="wrong_data")
									return HttpResponseRedirect('/mla/get-tin-info/')
								
							else:
								 
								try:

									 
									individual = Individual.objects.get(tin = tin_obj.id)

									if vehicle_category ==  "Private Vehicle Saloon" or vehicle_category == "Commercial Vehicle Saloon" or vehicle_category == "Private Pickup/Bus" or vehicle_category == "Commercial Pickup/Bus" or vehicle_category == "Dealers Vehicle":
										engine_size = True
										no_of_tyres = False
										engine_category = False

										
									elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
										no_of_tyres = True
										engine_size = False
										engine_category = False

										

									elif vehicle_category == "Commercial Tricycle/Motorcycle" or vehicle_category == "Private Motorcycle" or vehicle_category == "Dealers Tricycle/Motorcycle":
										engine_category = True
										no_of_tyres = False
										engine_size = False

									tin = individual.tin
									name = individual.name
									gender = individual.gender
									state = individual.state
									address = individual.address
									occupation = individual.occupation

									passport_pic_url = individual.passport_pic_url

									  
									return render(req, 'add_vehicle.html', {'vehicle_category':vehicle_category, "passport_pic_url":passport_pic_url, 'current_owner_tin':tin.tin, 'name':name, 'gender':gender, 'state':state, 'address':address, 'occupation':occupation, "register_for":"individual",  "engine_size":engine_size, "no_of_tyres":no_of_tyres, "engine_category":engine_category}) 

								except Individual.DoesNotExist:
									 
									messages.info(req, "Tin Does Not Exist", extra_tags = "wrong_tin")
									return HttpResponseRedirect('/mla/get-tin-info/')
					else:
						 
						messages.info(req, "Tin Does Not Exist", extra_tags = "wrong_tin")
						return HttpResponseRedirect('/mla/get-tin-info/')


				
				else:					
					messages.info(req, "invalid form fields", extra_tags="wrong_data")
					return HttpResponseRedirect('/mla/get-tin-info/')


				
			else:				
				return render(req, 'get_tin_info.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		  
		return render(req, 'login.html')




def vehicle_record_preview(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA User' or "Super Administrator":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/mla/get-tin-info/')

			elif req.method == "POST" and req.POST:

				user_id = req.session.get("user_id")

				form = VehicleForm(req.POST)


				if  form.is_valid():

					try:
						
						staff_obj = User.objects.get(id = user_id)
						office_obj = Office.objects.get(id = staff_obj.office.id)

						plate_number_obj = form.cleaned_data.get("number_plate")
 
					 	 
						if  plate_number_obj.is_taken:
							 
							messages.info(req, "Plate Taken", extra_tags = "plate_taken")
							
							return render(req, 'add_vehicle.html')
							
						elif  not plate_number_obj.is_issued:
							messages.info(req, "Plate Issued", extra_tags = "plate_not_issued")
							
							return render(req, 'add_vehicle.html')
							
					 		

						elif plate_number_obj.office.office_name != plate_number_obj.office.office_name:
							messages.info(req, "Plate no for office", extra_tags = "plate_not_for_office")
							return render(req, 'add_vehicle.html')

						elif (plate_number_obj.office.office_name == plate_number_obj.office.office_name) :
							
							current_owner_tin = req.POST.get('current_owner_tin')

							chassis_number = form.cleaned_data.get("chassis_number")
							vehicle_model = form.cleaned_data.get("vehicle_model")
							
							vehicle_category = form.cleaned_data.get("vehicle_category")
							gross_weight = form.cleaned_data.get("gross_weight")
							net_weight = form.cleaned_data.get("net_weight")
							no_of_passengers = form.cleaned_data.get("no_of_passengers")
							colour = form.cleaned_data.get("colour")			 
							engine_size = req.POST.get("engine_size", "-")
							cost_price = req.POST.get("cost_price", "-")
							engine_category = req.POST.get("engine_category", "-")
							no_of_tyres = req.POST.get("no_of_tyres", "-")

						 


							if net_weight >= gross_weight:
								messages.info(req, "gross less than net", extra_tags = "net_gt_gross")
								return render(req, 'add_vehicle.html')

							weight = int(gross_weight) - int(net_weight)
							messages.info(req, "Plate Taken", extra_tags = "record_preview")

							data_context = {'current_owner_tin':current_owner_tin, 'chassis_number':chassis_number, 'engine_category':engine_category, 'no_of_tyres':no_of_tyres,  'vehicle_model':vehicle_model, 'number_plate':plate_number_obj, 'vehicle_category':vehicle_category, 'gross_weight':gross_weight, 'net_weight':net_weight, 'no_of_passengers':no_of_passengers, 'colour':colour, 'weight':weight, 'engine_size':engine_size, 'cost_price':cost_price }
							
							messages.success(req, " Record Preview ",  extra_tags = 'record_preview data' )
							return render(req, 'add_vehicle.html', data_context)

						else:
							
							return HttpResponseRedirect('/mla/get-tin-info/')
							 

					except User.DoesNotExist as e:
						messages.info(req, " wrong data", extra_tags="wrong_data")
						return HttpResponseRedirect('/mla/get-tin-info/')

					except Office.DoesNotExist as e:
						 
						messages.info(req, " wrong data", extra_tags="wrong_data")
						return HttpResponseRedirect('/mla/get-tin-info/')

					except Exception as e:
						print(e)				 
						messages.info(req, " wrong data", extra_tags="wrong_data")
						 
				else:
					  
					if form['chassis_number'].errors: 
						messages.info(req, "wrong chassis number", extra_tags = "chassis_exist")
						return render(req, 'add_vehicle.html')

					elif form['number_plate'].errors:
						
						messages.info(req, "wrong data", extra_tags = "wrong_plate")
						return render(req, 'add_vehicle.html')
						
					else:
						messages.info(req, "wrong data", extra_tags = "wrong_data")
						return render(req, 'add_vehicle.html')

					
				
			else:				
				return HttpResponseRedirect('/mla/get-tin-info/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		 	 
		return render(req, 'login.html')


def save_vehicle(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA User' or "Super Administrator":		 

			if req.method == "GET":
				 			
				return HttpResponseRedirect('/mla/get-tin-info/')

			elif req.method == "POST" and req.POST:				 
				user_id = req.session.get("user_id")

				current_owner_tin = req.POST.get('current_owner_tin')
				chassis_number = req.POST.get("chassis_number")
				vehicle_model = req.POST.get("vehicle_model")
				number_plate = req.POST.get("number_plate")
				vehicle_category = req.POST.get("vehicle_category")
				gross_weight = req.POST.get("gross_weight")
				net_weight = req.POST.get("net_weight")
				weight = req.POST.get("weight")
				no_of_passengers = req.POST.get("no_of_passengers")
				colour = req.POST.get("colour")			 
				engine_size = req.POST.get("engine_size", "-")
				cost_price = req.POST.get("cost_price", "-")
 
				engine_category = req.POST.get("engine_category", "-")
				no_of_tyres = req.POST.get("no_of_tyres", "-")
			  
				

				add_with_particulars = req.POST.get("add_with_particulars", False)
				 
 				 
				tin_obj = AssignedTin.objects.get(tin = current_owner_tin)
				number_plate_obj = NumberPlate.objects.get(number_plate=number_plate, is_taken=False)
				staff_obj = User.objects.get(id = user_id)
				 
				try:
					if add_with_particulars:
					
						vehicle_obj =  Vehicle( current_owner_tin= tin_obj, chassis_number = chassis_number,  vehicle_model = vehicle_model,number_plate = number_plate_obj, vehicle_category = vehicle_category, gross_weight =gross_weight , net_weight = net_weight, no_of_passengers = no_of_passengers, colour = colour, weight = weight, engine_size =engine_size, cost_price = cost_price, staff = staff_obj)

						bill_results = generate_assessment_bill(vehicle_category, tin_obj, engine_size, cost_price, chassis_number, staff_obj) 
						
						if bill_results == "charge_unavailable":
							messages.success(req, "Charge not available", extra_tags= "charge_unavailable")
							return render(req, 'add_vehicle.html')

						elif bill_results == "uncaught_exception":
							messages.success(req, "Exception", extra_tags= "uncaught_exception")
							return render(req, 'add_vehicle.html')
						
						else:		
							number_plate_obj.is_taken = True
							number_plate_obj.is_issued = True
							number_plate_obj.assigned_to_acar_by = staff_obj
							print(bill_results)
							transaction_assessments =  TransactionAssessment.objects.filter(transaction_code = bill_results,  chassis_number  =  chassis_number, tin = tin_obj.id)

							number_plate_obj.save()
							vehicle_obj.save()
 					
							messages.success(req, " Record Created", extra_tags= "assessment_preview")
							
							return render(req, 'add_vehicle.html', {'transaction_code':bill_results, 'transaction_assessments':transaction_assessments, 'vehicle_obj':vehicle_obj})
							  
					else:
						 
						vehicle_obj = Vehicle( current_owner_tin= tin_obj, chassis_number = chassis_number,  vehicle_model = vehicle_model,number_plate = number_plate_obj, vehicle_category = vehicle_category, gross_weight =gross_weight , net_weight = net_weight, no_of_passengers = no_of_passengers, colour = colour, weight = weight, engine_size =engine_size, cost_price = cost_price, staff = staff_obj)
						number_plate_obj.is_taken = True
						number_plate_obj.is_issued = True
						 
						number_plate_obj.assigned_to_acar_by = staff_obj
						number_plate_obj.save()
						vehicle_obj.save()
						messages.success(req, " Record Created", extra_tags= "record_created")
						return HttpResponseRedirect('/mla/get-tin-info/')

				except NumberPlate.DoesNotExist:
						print(e)						
						messages.success(req, " Record Exist", extra_tags= "plate_taken")
						return render(req, 'add_vehicle.html')
				
				except Exception as e:
						print(e)					
						messages.success(req, " Record Exist", extra_tags= "record_already_created")
						return render(req, 'add_vehicle.html')
						  

					
			else:
				 
				return HttpResponseRedirect('/mla/get-tin-info/')		 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		  
		return render(req, 'login.html')

def change_vehicle_ownership(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA User' or "Super Administrator":

			
			if req.method == "POST" and req.POST: 		 
						 
				form = SingleValueCharFieldForm(req.POST)

				if form.is_valid(): 
					chassis_number = form.cleaned_data.get("search_text")

					try:
						vehicle_obj = Vehicle.objects.get(chassis_number = chassis_number)

						if vehicle_obj.theft_status:

							messages.success(req, "Vehicle is stolen ", extra_tags= "vehicle_stolen")
							return render(req, 'get_tin_info_ch_ownership.html')


						else:						 
							current_owner_tin = AssignedTin.objects.get(tin = vehicle_obj.current_owner_tin.tin)
						 
							if current_owner_tin.tin_for == "Individual":
								individual_obj = Individual.objects.filter(tin = current_owner_tin.id).first()
			  
								return render(req, 'view_to_change_vehicle_ownership.html', {"vehicle_for":"individual", 'vehicle_obj':vehicle_obj, 'individual_obj':individual_obj} )	

								
							else:
								 
								company_obj  = Company.objects.filter(tin = current_owner_tin.id).first()								   
								return render(req, 'view_to_change_vehicle_ownership.html', {"vehicle_for":"company", 'vehicle_obj':vehicle_obj, 'company_obj':company_obj} )	
													

					except Vehicle.DoesNotExist:
						messages.success(req, "warning", extra_tags= "wrong_chassis")
						return render(req, 'get_tin_info_ch_ownership.html')	
				else:
					messages.success(req, "wrong data", extra_tags= "dwrong_data")
					return render(req, 'get_tin_info_ch_ownership.html')	
 
				
			else:
				return render(req, 'get_tin_info_ch_ownership.html')			

			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		 		 
		return render(req, 'login.html')


 
	
def save_change_of_ownership(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA User' or "Super Administrator":

			if req.method == "POST" and req.POST: 		 
				form = TINForm(req.POST)

				if form.is_valid(): 

					current_vehicle_owners_tin_number = req.POST.get("current_owners_tin")
					new_vehicle_owners_tin_number = form.cleaned_data.get("tin_number")

					try:			 
						new_owner_tin_obj = AssignedTin.objects.get(tin = new_vehicle_owners_tin_number)			  

						vehicle_obj = Vehicle.objects.get(current_owner_tin = current_vehicle_owners_tin_number)
						 
						 
						 
						if vehicle_obj.current_owner_tin.tin == new_owner_tin_obj.tin:
							 
							messages.info(req, " warning ", extra_tags = "transaction_between_same_tin")
							return render(req, 'view_to_change_vehicle_ownership.html')

						
						amount = None

						if vehicle_obj.vehicle_category == "Private Vehicle Saloon" or vehicle_obj.vehicle_category == "Private Pickup/Bus" or vehicle_obj.vehicle_category == "Commercial Vehicle Saloon" or vehicle_obj.vehicle_category == "Commercial Pickup/Bus" or vehicle_obj.vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":

							charge_others_obj =  ChargesOthers.objects.get(particulars ='Change of ownership' )
							amount = charge_others_obj.amount

						else:				 

							charge_others_change_ownership_TM =  ChargesOthers.objects.get(particulars ='Change of ownership (TM)' )
							amount = charge_others_obj.amount 
						
						user_id = req.session.get("user_id")

						staff_obj = User.objects.get(id = user_id)
						
						vehicle_obj.old_owners_tin = vehicle_obj.current_owner_tin.tin			
						vehicle_obj.current_owner_tin = new_owner_tin_obj

						transaction_code = t_code()

						transaction_assessment = TransactionAssessment(transaction_code = transaction_code, tin = new_owner_tin_obj, chassis_number  =  vehicle_obj.chassis_number, particulars = "Change of ownership", amount = amount, staff = staff_obj)

						
						 
						bill_results = generate_assessment_bill_change_ownership(transaction_code, new_owner_tin_obj, vehicle_obj.vehicle_category, vehicle_obj.engine_size, vehicle_obj.cost_price, vehicle_obj.chassis_number, staff_obj)
 

						if bill_results == "charge_unavailable":
							messages.success(req, "Charge not available", extra_tags= "charge_unavailable")
							return render(req, 'add_vehicle.html')

						elif bill_results == "uncaught_exception":
							messages.success(req, "Exception", extra_tags= "uncaught_exception")
							return render(req, 'add_vehicle.html')
						else:
							transaction_assessment.save()
							vehicle_obj.save()
							 
							transaction_assessments = TransactionAssessment.objects.filter(transaction_code = bill_results, chassis_number  = vehicle_obj.chassis_number, tin = new_owner_tin_obj)
							messages.success(req, "success", extra_tags = "change_successfull")
							return render(req, 'view_to_change_vehicle_ownership.html', { 'transaction_code':transaction_code, 'transaction_assessments':transaction_assessments,'new_vehicle_owner_obj':new_owner_tin_obj, 'vehicle_obj':vehicle_obj })
		
						

							
					except AssignedTin.DoesNotExist:
						messages.success(req, "wrong_tin", extra_tags= "wrong_tin")
						return render(req, 'view_to_change_vehicle_ownership.html' )

					except ChargesOthers.DoesNotExist:
						messages.success(req, "wrong_tin", extra_tags= "charge_unavailable")
						return render(req, 'view_to_change_vehicle_ownership.html' )

					except Vehicle.DoesNotExist:


						messages.success(req, "wrong_tin", extra_tags= "wrong_data")
						return render(req, 'view_to_change_vehicle_ownership.html' )
					
					except Exception as e:
						 
						messages.success(req, "No vehicle with this tin Created", extra_tags= "uncaught_exception")
						return render(req, 'view_to_change_vehicle_ownership.html' )
						 
				else:
					messages.success(req, "wrong data", extra_tags= "wrong_data")
					return render(req, 'view_to_change_vehicle_ownership.html' )

			else:
				return render(req, 'get_tin_info_ch_ownership.html') 
 
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		 		 
		return render(req, 'login.html')


			

	

def mark_stolen_vehicle(req, plate_id = ""):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA User' or "Super Administrator":

			if req.method == "POST" and req.POST:
				form = PlateNumberForm(req.POST)

				if form.is_valid():
					number_plate = form.cleaned_data.get("number_plate")

					try:
						vehicle_obj =  Vehicle.objects.get(number_plate = number_plate)
						individal_obj = Individual.objects.get(tin = vehicle_obj.current_owner_tin)						 

						return render(req, 'view_to_mark_vehicle_theft.html', {'vehicle_obj':vehicle_obj, "individal_obj":individal_obj})

					except Vehicle.DoesNotExist:
						messages.success(req, "wrong plate", extra_tags= "wrong_plate_number")
						return render(req, 'get_plate_info_mark_stolen.html')

					except Individual.DoesNotExist:
						 
						vehicle_obj =  Vehicle.objects.get(number_plate = number_plate)
						company_obj = Company.objects.get(tin = vehicle_obj.current_owner_tin)

						return render(req, 'view_to_mark_vehicle_theft.html', {'vehicle_obj':vehicle_obj, "company_obj":company_obj})

					except Company.DoesNotExist:						 
						messages.success(req, "Wrong Tin", extra_tags= "wrong_plate_number")
						return render(req, 'get_plate_info_mark_stolen.html')
						
						 
						
					
						 
				else:
					messages.success(req, "wrong data", extra_tags= "wrong_data")
					return render(req, 'get_plate_info_mark_stolen.html')

					 
							
			else:				
				return render(req, 'get_plate_info_mark_stolen.html', {"plate_id":plate_id})			 

					 
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		 
		return render(req, 'login.html')

def mark_vehicle(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		 
			if req.method == "POST" and req.POST:


				

				form = PlateWithPassForm(req.POST) 

				if form.is_valid():			 

					plate_id = form.cleaned_data.get("number_plate")				 
					paswd = form.cleaned_data.get("password")

					try:
						user_id = req.session['user_id']
						user = User.objects.get(id = user_id)

						if user.password == crypt(paswd, user.password):

							
							vehicle_obj = Vehicle.objects.get(number_plate = plate_id)

							if  vehicle_obj.theft_status:
								new_state = False
								notification = Notification(notification_for= "Vehicle", notification_type = "Change", notification_txt = "User with ID:"+str(user.id)+	" change VEHICLE:"+vehicle_obj.number_plate.number_plate+" theft status From  = "+ str(vehicle_obj.theft_status) +", To Theft Stat = "+str(new_state), generated_by= user)
								
								vehicle_obj.theft_status = False								
								vehicle_obj.save()
								notification.save()

								messages.info(req, "success", extra_tags = "change_successfull")
								return render(req, 'get_plate_info_mark_stolen.html')

							else:
								new_state = False
								notification = Notification(notification_for= "Vehicle", notification_type = "Change", notification_txt = "User with ID:"+str(user.id)+	" change VEHICLE:"+vehicle_obj.number_plate.number_plate+" theft status From  = "+str(vehicle_obj.theft_status) +", To Theft Stat = "+str(new_state), generated_by= user)
						
								vehicle_obj.theft_status = True
								vehicle_obj.save()
								notification.save()

								messages.info(req, "success", extra_tags = "change_successfull")
								return render(req, 'get_plate_info_mark_stolen.html')
  
	 
						else:						 
							messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
							return render(req, 'view_to_mark_vehicle_theft.html')

					except User.DoesNotExist:
						return render(req, 'get_plate_info_mark_stolen.html')

					 
				else:
					print(form.errors)				  
					return render(req, 'get_plate_info_mark_stolen.html')



			else:
				return render(req, 'get_plate_info_mark_stolen.html')
 
	else:
		 	 
		return render(req, 'login.html')


def get_tin_info_learners_permit(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA User' or "Super Administrator":

			
			if req.method == "POST" and req.POST: 		 
				form = TINForm(req.POST)
				if form.is_valid():
					tin_number = form.cleaned_data.get("tin_number")

					try:
						assigned_tin = AssignedTin.objects.get(tin = tin_number, tin_for = "Individual")
						individal_obj =  Individual.objects.get(tin = assigned_tin.id)

						transaction_code = t_code()
						expiration_date = expirationdate_1year
			  
						 
						return render(req, 'learners_permit.html', {'individal_obj':individal_obj, "transaction_code":transaction_code,"expiration_date":expiration_date})
						
					except AssignedTin.DoesNotExist: 
						messages.success(req, "wrong wrong", extra_tags= "wrong_tin")
						return render(req, 'get_tin_info_learner_permit.html')	

					except Individual.DoesNotExist:
						# wrong tin
						messages.success(req, "wrong wrong", extra_tags= "wrong_tin") 
						return render(req, 'get_tin_info_learner_permit.html')			 
				else:
					messages.success(req, "wrong wrong", extra_tags= "wrong_data") 
					return render(req, 'get_tin_info_learner_permit.html')
				
			else:				
				return render(req, 'get_tin_info_learner_permit.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		 
		return render(req, 'login.html')


def save_learners_permit(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):	
				 
		if req.method == "POST" and req.POST: 		 
			user_id = req.session.get("user_id")

			tin_number = req.POST.get("individual_tin")	 
			transaction_code = req.POST.get('transaction_code') 
			expiration_date = req.POST.get('expiration_date')
			particulars_option = req.POST.get('particulars')

			try:
				
				# check if expiration date has not epired
				tin_obj = AssignedTin.objects.get(tin = tin_number, tin_for = "Individual") 
				 
				LearnersPermit.objects.get(learners_tin = tin_obj.id, is_active = True)

				messages.success(req, "Valid permit", extra_tags= "permit_still_valid")
				return render(req, 'learners_permit.html')



			except LearnersPermit.DoesNotExist:

				try:
					user_obj = User.objects.get(id = user_id) 

					 
					charge_others =	ChargesOthers.objects.get( particulars = 'Learners Permit')
					learners_permit_amount = charge_others.amount

					charge_others_lsymbol = ChargesOthers.objects.get( particulars='L-Symbol' )				
					lsymbol_amount = charge_others_lsymbol.amount

					#Get sms amount
					charge_others_sms_amount = ChargesOthers.objects.get( particulars='SMS Alert' )				
					sms_amount = charge_others_sms_amount.amount

					#Get Stamp Duty Amount
					charge_others_stamp_duty = ChargesOthers.objects.get(particulars = 'Stamp Duty')
					stamp_duty_amount = charge_others_stamp_duty.amount

					user_id = req.session.get("user_id")
					staff_obj = User.objects.get(id = user_id)

					individal_obj =  Individual.objects.get(tin = tin_obj.id)	

						 
							 
					
					if(particulars_option == "Permit Only"):

											 
						
						transaction_assessment_lP = TransactionAssessment(transaction_code = transaction_code, tin = tin_obj, particulars = "Learners Permit", amount = learners_permit_amount, expiration_date =  expiration_date, transaction_type = 'Learners Permit', staff = staff_obj) 
					 	 
						transaction_assessment_sms_alert = TransactionAssessment(transaction_code = transaction_code, tin = tin_obj, amount = sms_amount,  particulars =  "SMS Alert", transaction_type = 'SMS Alert',staff = staff_obj) 
												
						transaction_assessment_stamp_d = TransactionAssessment(transaction_code = transaction_code, tin = tin_obj, particulars="Stamp Duty", amount = stamp_duty_amount,  transaction_type = 'Stamp Duty',staff = staff_obj) 

						learners_permit = LearnersPermit(transaction_code = transaction_code, learners_tin = tin_obj, expiration_date = expiration_date, particulars = "Permit Only", amount = learners_permit_amount+sms_amount+stamp_duty_amount , staff = staff_obj) 

						
						transaction_assessment_lP.save()
						transaction_assessment_sms_alert.save()
						transaction_assessment_stamp_d.save()
						learners_permit.save()
					
						transaction_assessments = TransactionAssessment.objects.filter(transaction_code = transaction_code, tin = tin_obj)	
						
						messages.info(req, "record added Successfully", extra_tags = "record_created")
						return render(req, 'learners_permit.html',  {'t_code':transaction_code, "transaction_assessments":transaction_assessments, "individal_obj":individal_obj})					
						                           


					
					elif(particulars_option == "Permit and L-Symbol"):
						#SAVE INTO ASSESSMENT TRANSACTION
						transaction_assessment_lP = TransactionAssessment(transaction_code = transaction_code, tin = tin_obj, amount = learners_permit_amount + lsymbol_amount, particulars = "Learners Permit + L-Symbol", transaction_type = 'Learners Permit', expiration_date = expirationdate_1year,staff = staff_obj) 
					 
						#SAVE INTO ASSESSMENT TRANSACTION
						transaction_assessment_sms_alert = TransactionAssessment(transaction_code = transaction_code, tin = tin_obj, particulars="SMS Alert", amount = sms_amount, transaction_type = 'SMS Alert', staff = staff_obj) 
						
						  
		 
						transaction_assessment_stamp_d = TransactionAssessment(transaction_code = transaction_code, tin = tin_obj,particulars="Stamp Duty", amount = stamp_duty_amount, transaction_type = 'Stamp Duty',staff = staff_obj) 
						learners_permit = LearnersPermit(transaction_code = transaction_code, learners_tin = tin_obj, expiration_date = expiration_date, particulars = "Permit and L-Symbol", amount = float(learners_permit_amount+sms_amount+stamp_duty_amount+lsymbol_amount), staff = staff_obj) 

						transaction_assessment_lP.save()
						transaction_assessment_sms_alert.save()
						transaction_assessment_stamp_d.save()
						learners_permit.save()

						transaction_assessments = TransactionAssessment.objects.filter(transaction_code = transaction_code, tin=tin_obj, is_expired = False)	

						messages.info(req, "Success", extra_tags = "record_created")
						return render(req, 'learners_permit.html',  {'t_code':transaction_code, "transaction_assessments":transaction_assessments, "individal_obj":individal_obj})

				except ChargesOthers.DoesNotExist as e: 
					messages.success(req, "Vehicle Record Created", extra_tags= "others_charge_unavailable")
					HttpResponseRedirect('mla/get-learners-permit')	
					
					
				 
				except Exception as e:
					print(e)
					return HttpResponseRedirect('/mla/get-learners-permit/')	

		else:
			HttpResponseRedirect('mla/get-learners-permit')			

				
	else:
		  
		return render(req, 'login.html')


 
	


def get_chassisnumber_info_vehicle_revalidation(req):
	user_access_level  = req.session.get("access_level")


	if 'user_id' in req.session  and ('access_level' in req.session):	
			
			if req.method == "POST" and req.POST: 		 
				form = ChassisNumberFieldForm(req.POST)
				if form.is_valid():
					chassis_number = form.cleaned_data.get("chassis_number")
					
					vehicle_obj = None

					try:
						
						vehicle_obj = Vehicle.objects.get(chassis_number = chassis_number)
						individual_obj = Individual.objects.get(tin = vehicle_obj.current_owner_tin.id)			 

						return render(req, 'view_to_change_vehicle_revalidation.html', {'vehicle_owner_tin':individual_obj.tin.tin,"vehicle_owner_type":vehicle_obj.current_owner_tin.tin_for, "vehicle_owner_name":individual_obj.name, 'vehicle_obj':vehicle_obj})


					except Individual.DoesNotExist:

						company_obj = Company.objects.get(tin = vehicle_obj.current_owner_tin.id)	
						 
						return render(req, 'view_to_change_vehicle_revalidation.html', {'vehicle_owner_tin':company_obj.tin.tin,"vehicle_owner_type":vehicle_obj.current_owner_tin.tin_for, "vehicle_owner_name":company_obj.bussiness_name, 'vehicle_obj':vehicle_obj})


					except Company.DoesNotExist as e:	
						print(e)					
						messages.success(req, "Invalid chassis", extra_tags= "error")
						return render(req, 'get_tin_info_revalidation.html')	


					except Vehicle.DoesNotExist:
						
						messages.success(req, "Invalid chassis number", extra_tags= "wrong_chassis")
						return render(req, 'get_tin_info_revalidation.html')		 

						 
				else:
					
					messages.success(req, "Invalid chassis number", extra_tags= "error")
					return render(req, 'get_tin_info_revalidation.html')
				
			else:				
				return render(req, 'get_tin_info_revalidation.html')			 

		 
	else:		 	 
		return render(req, 'login.html')




def save_vehicle_revalidation(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		 
			
			if req.method == "POST" and req.POST: 		 
				 
				form = PlateNumberObjForm(req.POST)
				if form.is_valid():
					new_plate_number_obj = form.cleaned_data.get("number_plate")
					
					chassis_number = req.POST.get('chassis_number')
					current_owner_tin = req.POST.get("current_owner_tin")

					user_id = req.session.get("user_id")
					staff_obj = User.objects.get(id = user_id) 

					try:
						# bfdgrdc
					 	 
						if  new_plate_number_obj.is_taken:							 
							messages.info(req, "Plate Taken", extra_tags = "plate_taken")
							
							return render(req, 'view_to_change_vehicle_revalidation.html')
							
						elif  not new_plate_number_obj.is_issued:
							messages.info(req, "Plate Issued", extra_tags = "plate_not_issued")							
							return render(req, 'view_to_change_vehicle_revalidation.html')
							
					 		

						elif new_plate_number_obj.office.office_name != new_plate_number_obj.office.office_name:
							messages.info(req, "Plate no for office", extra_tags = "plate_not_for_office")

							return render(req, 'view_to_change_vehicle_revalidation.html')

						elif (new_plate_number_obj.office.office_name == new_plate_number_obj.office.office_name) :
							print(chassis_number+"  "+new_plate_number_obj.number_plate+" "+current_owner_tin)

							vehicle_obj =  Vehicle.objects.get(chassis_number = chassis_number, number_plate=  new_plate_number_obj.number_plate, current_owner_tin = current_owner_tin)
 
							amount = None 

							if(vehicle_obj.vehicle_category == "Private Vehicle Saloon" or vehicle_obj.vehicle_category == "Private Pickup/Bus" or  vehicle_obj.vehicle_category == "Commercial Vehicle Saloon" or  vehicle_obj.vehicle_category == "Commercial Pickup/Bus" or  	vehicle_obj.vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper"):
							 	charge_others =  ChargesOthers.objects.get( particulars ='New Plate Number' )
							 	amount = charge_others.amount

							else:
								charge_others =  ChargesOthers.objects.get(particulars ='New Plate Number (TM)' )
								amount = charge_others.amount
						 
						 
							# SAVE INTO ASSESSMENT TRANSACTION
	 
	 
							transaction_code = t_code()
							old_plate_number = vehicle_obj.number_plate.number_plate
	 
							revalidatation = Revalidation(tin = vehicle_obj.current_owner_tin, old_plate_number = vehicle_obj.number_plate, new_plate_number = new_plate_number_obj, staff =staff_obj)
							vehicle_obj.number_plate = new_plate_number_obj
							# save
							 
							transaction_assessment = TransactionAssessment( transaction_code = transaction_code, tin = vehicle_obj.current_owner_tin, chassis_number = chassis_number, particulars = "New Plate Number", amount = amount, transaction_type = 'Revalidation',staff = staff_obj) 
							
							bill_results = generate_assessment_bill_vehicle_revalidation( vehicle_obj.vehicle_category, transaction_code, vehicle_obj.current_owner_tin,  vehicle_obj.engine_size,  vehicle_obj.cost_price,  vehicle_obj.chassis_number, staff_obj) 
	 
							 
							if bill_results == "charge_unavailable":
								print("")
								messages.success(req, "Charge not available", extra_tags= "charge_unavailable")
								return render(req, 'view_to_change_vehicle_revalidation.html')

							elif bill_results == "uncaught_exception":
								messages.success(req, "Exception", extra_tags= "uncaught_exception")
								return render(req, 'view_to_change_vehicle_revalidation.html')
							
							else:

								new_plate_number_obj.is_taken = True
								new_plate_number_obj.is_issued = True
								new_plate_number_obj.assigned_to_acar_by = staff_obj
								revalidatation.save()
								transaction_assessment.save()
								new_plate_number_obj.save()
								vehicle_obj.save()
								 
								transaction_assessments =  TransactionAssessment.objects.filter(transaction_code = bill_results,  chassis_number  =  chassis_number, tin = vehicle_obj.current_owner_tin.id)

															
	 					
								messages.success(req, " Record Created", extra_tags= "assessment_preview")

								
								return render(req, 'view_to_change_vehicle_revalidation.html', {'transaction_assessments':transaction_assessments, "tin_for":vehicle_obj.current_owner_tin.tin_for, 'vehicle_category':vehicle_obj.vehicle_category,  'old_plate_number':old_plate_number, 'new_plate_number':vehicle_obj.number_plate.number_plate ,'current_owner_tin':vehicle_obj.current_owner_tin.tin, 'chassis_number':vehicle_obj.chassis_number,})
						 
	 

					except ChargesOthers.DoesNotExist as e:
						messages.success(req, "ChargesOthers not available", extra_tags= "others_charge_unavailable")
						return render(req, 'view_to_change_vehicle_revalidation.html')	


					except Vehicle.DoesNotExist:
						messages.success(req, "ChargesOthers not available", extra_tags= "wrong_data")
						return render(req, 'get_tin_info_revalidation.html')		 

					except Exception as e:
						print(e)
						return render(req, 'get_tin_info_revalidation.html')
						 
						 
				else:
					 
					messages.success(req, "ChargesOthers not available", extra_tags= "wrong_plate")
					return render(req, 'view_to_change_vehicle_revalidation.html')	
	 
			else:
				HttpResponseRedirect('/mla/change-vehicle-revalidation/')			
	# return render(req, 'login.html')
		
	else:
		 		 
		return render(req, 'login.html')


def get_info_vehicle_assessment(req): 
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		
			if req.method == "POST" and req.POST:

				form = VehicleAssessmentForm(req.POST)
				if form.is_valid():
				 
					search_text = form.cleaned_data.get('search_text')	
					 

					try:
						vehicle_obj = Vehicle.objects.get(Q(number_plate = search_text) | Q(chassis_number = search_text))
						 
						if(vehicle_obj.theft_status):
							# vehicle stoen
							messages.info(req, "car stolen", extra_tags= "car_stolen_alert")
							return render(req, 'get_vehicle_info_vehicle_assessment.html')	

						else:
							
							  
							return render(req, 'vehicle_assessment.html', {'vehicle_obj':vehicle_obj})

					except Vehicle.DoesNotExist:
						 
						messages.success(req, "Wrong Tin", extra_tags= "wrong_search_text")
						return render(req, 'get_vehicle_info_vehicle_assessment.html')


					except Exception as e:
						print(e)
						return render(req, 'get_vehicle_info_vehicle_assessment.html')	

				else:
					return render(req, 'get_vehicle_info_vehicle_assessment.html')	

			else:
				 		
				return render(req, 'get_vehicle_info_vehicle_assessment.html')			 

		
	else:
		 	 
		return render(req, 'login.html') 
	
		 

			 
			
	 

def save_vehicle_assessment(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		 
			if req.method == "POST" and req.POST: 		 
				user_id = req.session.get("user_id")
				try:
					tin = req.POST.get('current_owner_tin')
					assessment_type = req.POST.get("assessment_type")

					chassis_number = req.POST.get('chassis_number') 
					number_plate = req.POST.get('number_plate')

					staff_obj = User.objects.get(id = user_id)					 
					tin_obj = AssignedTin.objects.get(tin  = tin)
					vehicle_obj = Vehicle.objects.get(number_plate = number_plate, chassis_number = chassis_number)	

						  

					transaction_assessments = TransactionAssessment.objects.filter(particulars = assessment_type, transaction_type = 'Renewal of Particulars', chassis_number =vehicle_obj.chassis_number, is_expired = False ).count()
					 
					if transaction_assessments > 0:
						messages.success(req, "Assesment still Valid  ", extra_tags= "assessement_still_valid")
						return  render(req, 'vehicle_assessment.html' )
					
					else:

						bill_results = generate_assessment_bill_vehicle_assessment(vehicle_obj.vehicle_category, assessment_type, tin_obj, vehicle_obj.chassis_number, staff_obj)

						if bill_results == "charge_unavailable":

							messages.success(req, "Charge not available", extra_tags= "charge_unavailable")
							return  render(req, 'vehicle_assessment.html' )

						elif bill_results == "uncaught_exception":

							messages.success(req, "Exception", extra_tags= "uncaught_exception")
							return  render(req, 'vehicle_assessment.html' )
						else:



							transaction_assessments  = TransactionAssessment.objects.filter(transaction_code = bill_results,  transaction_type = 'Renewal of Particulars', chassis_number = vehicle_obj.chassis_number, tin = tin_obj,  is_expired = False )
							messages.success(req, "Exception", extra_tags= "record_created")
							return  render(req, 'vehicle_assessment.html', {"transaction_assessments":transaction_assessments, "tin":vehicle_obj.current_owner_tin.tin, "chassis_number":chassis_number, "number_plate":number_plate} )
					
				except Exception as e:
					print(e)
					 
					messages.success(req, "Exception", extra_tags= "uncaught_exception")
					return  render(req, 'vehicle_assessment.html' )
 
			else :
				HttpResponseRedirect('/mla/get-vehicle-assessment/') 
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def vehicles(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'MLA User' or 'Super Administrator':			 
			vehicles = Vehicle.objects.all()
			
			return render(req, 'vehicles.html', {"vehicles":vehicles})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')


def learners(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'MLA User' or 'Super Administrator':			 
			learners_permits = LearnersPermit.objects.all()
			
			return render(req, 'learners.html', {"learners_permits":learners_permits})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')