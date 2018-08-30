from django.shortcuts import render
from random import randint 
from django.http import JsonResponse
from pbkdf2 import crypt

import base64
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt


from tin.models import  Individual, Company, AssignedTin
from setup.models import  StateCode, User, Office, LocalGovArea, InstitutionType, InstitutionCategory, Notification
from tin.forms import IndividualForm, CompanyForm, EditIndividualForm, EditCompanyForm

from django.contrib import messages


from django.http import HttpResponseRedirect


def generate_tin(req):
	 
    range_start = 10**(6-1)
    range_end = (10**6)-1
   
    local_government_area_code = req.POST.get("lga")
    generated_rand_num =  randint(range_start, range_end)
    try:
    	
    	state_code_obj = StateCode.objects.get(id=1)
    	print(local_government_area_code)
    	tin = str(state_code_obj.state_code+local_government_area_code+str(generated_rand_num))
    	return tin

    except StateCode.DoesNotExist:
    	messages.success(req, " Record Preview ",  extra_tags = 'state_code_not_set' )    	 
    	return HttpResponseRedirect("") 



def vehicles(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator' or 'TIN User':			 
			vehicles = Vehicle.objects.all()
			
			return render(req, 'vehicles.html', {"vehicles":vehicles})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')

def companies(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator' or 'TIN User':
			 
			companies = Company.objects.all()			
		 
			return render(req, 'companies.html', {"companies":companies})				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')

def individaul_record_preview(req):

	 
	form = IndividualForm(req.POST)

	if form.is_valid():
		
	
		try:			
			new_tin = generate_tin(req)
			if len(new_tin) == 10:
				print(new_tin)				
				tin_obj = AssignedTin.objects.filter(tin = new_tin)

				while tin_obj.exists():
					new_tin = generate_tin(req)
					tin_obj = AssignedTin.objects.filter(tin = new_tin)


				title = req.POST.get("title")
				name = form.cleaned_data.get("name")
				gender = form.cleaned_data.get("gender")
				date_of_birth = form.cleaned_data.get("date_of_birth")
				marital_status = form.cleaned_data.get("marital_status")
				state = form.cleaned_data.get("state")
				address = form.cleaned_data.get("address")
				phone = form.cleaned_data.get("phone")
				email = form.cleaned_data.get("email")
				occupation = form.cleaned_data.get("occupation")
				employment_status = form.cleaned_data.get("employment_status")
				work_place = form.cleaned_data.get("work_place")

				try:


					
					User.objects.get(Q(email = email) | Q(phone = phone))
					messages.success(req, " Record Preview ",  extra_tags = 'email_taken' )
					return render(req, 'add_individual.html')
				except Exception as e:

					data_context = {"tin":new_tin, 'name':title+" "+name, 'gender':gender, 'date_of_birth':date_of_birth, 'marital_status':marital_status, 'state':state, 'address':address, 'phone':phone, 'email':email, 'occupation':occupation, 'employment_status':employment_status, 'work_place':work_place }
				
					messages.success(req, " Record Preview ",  extra_tags = 'record_preview' )
					return render(req, 'add_individual.html', data_context)

			else:
				 
				return HttpResponseRedirect('/tin/add-individual/')
				 		
		except Exception as e:
			print(e)			 
			messages.info(req, "uncaught Exception")
			return HttpResponseRedirect('/tin/add-individual/')	

		 
		 
	else:
		 
		messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
		return HttpResponseRedirect('/tin/add-individual/')

 


def save_individual(req):

	signed_in_user_id = req.session.get("user_id")
	try:		
		
		tin = req.POST.get("tin")
		name = req.POST.get("name")
		gender = req.POST.get("gender")
		date_of_birth = req.POST.get("date_of_birth")
		marital_status = req.POST.get("marital_status")
		state = req.POST.get("state")
		address = req.POST.get("address")
		phone = req.POST.get("phone")
		email = req.POST.get("email")
		occupation = req.POST.get("occupation")
		employment_status = req.POST.get("employment_status")
		work_place = req.POST.get("work_place")

		staff_obj = User.objects.get(id = signed_in_user_id)
		
		
		check_tin =  AssignedTin.objects.filter(tin = tin)

		if check_tin.exists():
			messages.success(req, "Individual record already created", extra_tags= "record_already_created")
			return HttpResponseRedirect('/tin/add-individual/')
		else:
			tin_obj = AssignedTin.objects.create(tin = tin,  tin_for = "Individual")
			Individual.objects.create(tin = tin_obj, name = name, gender = gender, date_of_birth = date_of_birth, marital_status = marital_status, state = state, address = address, phone = phone, email = email, occupation = occupation, employment_status = employment_status, work_place= work_place,  staff = staff_obj)
			
			messages.success(req, "User Record Created", extra_tags= "record_created")
			return HttpResponseRedirect('/tin/add-individual/')

		
	except User.DoesNotExist as e:
		messages.success(req, "User Record Created", extra_tags= "wrong_data")
		return HttpResponseRedirect('/tin/add-individual/')

	except Office.DoesNotExist as e:
		messages.success(req, "User Record Created", extra_tags= "wrong_data")
		return HttpResponseRedirect('/tin/add-individual/')

	except Exception: 
		return HttpResponseRedirect('/tin/add-individual/')
		 

def company_record_preview(req):

	user_access_level  = req.session.get("access_level")
	 
	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator" or "TIN User":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/tin/add-company/')

			elif req.method == "POST" and req.POST:

				form = CompanyForm(req.POST)

				if form.is_valid():
					
				
					try:			
						new_tin = generate_tin(req)
						if len(new_tin) == 10:					
							tin_obj = AssignedTin.objects.filter(tin = new_tin)

							while tin_obj.exists():
								new_tin = generate_tin(req)
								tin_obj = AssignedTin.objects.filter(tin = new_tin)

							institution_type = req.POST.get("institution_type")
							institution_category = req.POST.get("institution_category")
							lga = req.POST.get("lga")



							institution = form.cleaned_data.get("institution")
							bussiness_status = form.cleaned_data.get("bussiness_status")
							bussiness_class = form.cleaned_data.get("bussiness_class")
							registration_number = form.cleaned_data.get("registration_number")
							bussiness_ownership_type = form.cleaned_data.get("bussiness_ownership_type")
							bussiness_name = form.cleaned_data.get("bussiness_name")
							bussiness_owner = form.cleaned_data.get("bussiness_owner")
							bussiness_address = form.cleaned_data.get("bussiness_address")
							phone_number = form.cleaned_data.get("phone_number")
							email = form.cleaned_data.get("email")
							  
							local_government = LocalGovArea.objects.get(local_government_code = lga)



							try: 
								Company.objects.get(institution = institution, bussiness_class = bussiness_class,bussiness_status=bussiness_status,	 registration_number=registration_number,bussiness_ownership_type=bussiness_ownership_type,bussiness_name=bussiness_name,bussiness_owner = bussiness_owner,bussiness_address=bussiness_address,phone_number=phone_number,email=email)
 
								messages.success(req, "Exist",  extra_tags = 'record_already_created' )
								return render(req, 'add_company.html')
							
							except Company.DoesNotExist: 
								data_context = {'tin':new_tin, 'lga':local_government.local_government_name, 'institution':institution, 'institution_type':institution_type, 'institution_category':institution_category,   'bussiness_status':bussiness_status, 'bussiness_class':bussiness_class,'registration_number':registration_number, 'bussiness_ownership_type':bussiness_ownership_type, 'bussiness_name':bussiness_name, 'bussiness_owner':bussiness_owner, 'bussiness_address':bussiness_address, 'phone_number':phone_number, 'email':email } 
								messages.success(req, "Record Preview",  extra_tags = 'company_preview' )
								return render(req, 'add_company.html', data_context)

						else:
							 
							return HttpResponseRedirect('/tin/add-company/')
							 		
					except Exception as e:				 			 
						 
						return HttpResponseRedirect('/tin/add-company/')	

					except User.DoesNotExist:					 
						messages.success(req, "Wrong Data", extra_tags= "wrong_data")
						return render(req, 'add_company.html')	

					except Office.DoesNotExist:					 
						messages.success(req, "Wrong Data", extra_tags= "wrong_data")
						return render(req, 'add_company.html')	
		
					
				else:
					 
					messages.success(req, "Wrong Data", extra_tags= "wrong_data")
					return render(req, 'add_company.html')	

				
			else:
				
				return HttpResponseRedirect('/tin/add-company/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		 	 
		return render(req, 'login.html')

def save_company(req):

	signed_in_user_id = req.session.get("user_id")
	try:
		lga = req.POST.get("lga")	
		tin = req.POST.get("tin")
		institution = req.POST.get("institution")
		bussiness_status = req.POST.get("bussiness_status")
		bussiness_class = req.POST.get("bussiness_class")
		registration_number = req.POST.get("registration_number")
		bussiness_ownership_type = req.POST.get("bussiness_ownership_type")
		bussiness_name = req.POST.get("bussiness_name")
		bussiness_owner = req.POST.get("bussiness_owner")
		bussiness_address = req.POST.get("bussiness_address")
		phone_number = req.POST.get("phone_number")
		email = req.POST.get("email")
		  
		institution_type = req.POST.get("institution_type")
		institution_category = req.POST.get("institution_category")

		staff_obj = User.objects.get(id = signed_in_user_id)

		 
		institution_type_obj = InstitutionType.objects.get(type_name = institution_type)
		institution_category_obj = InstitutionCategory.objects.get(category_name = institution_category)

 
		 
		check_tin =  AssignedTin.objects.filter(tin = tin)


		if check_tin.exists():
			
			 
			messages.success(req, "Company record already created", extra_tags= "record_already_created")
			return HttpResponseRedirect('/tin/add-company/')
		else:
			
			tin_obj = AssignedTin.objects.create(tin = tin,  tin_for = "Company")
			Company.objects.create(tin = tin_obj, local_government = lga, institution = institution, institution_type = institution_type_obj, institution_category = institution_category_obj, bussiness_status = bussiness_status, bussiness_class = bussiness_class,registration_number = registration_number, bussiness_ownership_type = bussiness_ownership_type, bussiness_name = bussiness_name, bussiness_owner = bussiness_owner, bussiness_address = bussiness_address, phone_number = phone_number, email = email, staff = staff_obj)

			messages.success(req, "User Record Created", extra_tags= "record_created") 
			return HttpResponseRedirect('/tin/add-company/')

		
	except Exception as e:

		print(e)
		return HttpResponseRedirect('/tin/add-company/')

 

def edit_individual(req, individual_id):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator" or "TIN User":

			if individual_id != "":

				try:
					individual_obj =  Individual.objects.get(id = individual_id)

					work_places  = Company.objects.all()

					return render(req, 'edit_individual_record.html', {'individual_obj':individual_obj, "work_places":work_places})
					
				except Individual.DoesNotExist:
					return HttpResponseRedirect('/tin/individuals/')
 
 
			else:
				 
				return HttpResponseRedirect('/tin/individuals/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def update_individual(req):

	 
	try:		
		form = EditIndividualForm(req.POST)

		if form.is_valid():
			
			paswd = form.cleaned_data.get("password")
			user_id = req.session['user_id']
			user = User.objects.get(id = user_id)

			if user.password == crypt(paswd, user.password):

				tin = req.POST.get("tin")

				name = form.cleaned_data.get("name")
				gender = form.cleaned_data.get("gender")
				date_of_birth = form.cleaned_data.get("date_of_birth")
				marital_status = form.cleaned_data.get("marital_status")
				state = form.cleaned_data.get("state")
				address = form.cleaned_data.get("address")
				phone = form.cleaned_data.get("phone")
				email = form.cleaned_data.get("email")
				occupation = form.cleaned_data.get("occupation")
				employment_status = form.cleaned_data.get("employment_status")
				work_place = form.cleaned_data.get("work_place")


				
				individual_obj = Individual.objects.get(tin = tin)

				notification = Notification(notification_for= "Individual", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" Edited Individual record ID:"+str(individual_obj.id)+" From Name = "+individual_obj.name+" Gender = "+individual_obj.gender+" DOB = "+individual_obj.date_of_birth+" M State = "+individual_obj.marital_status+" State = "+individual_obj.state+" Address = "+individual_obj.address+" Phone = "+individual_obj.phone+" Email = "+individual_obj.email+" Occupation = "+individual_obj.occupation+" Employement Status = "+individual_obj.employment_status+" Work Place= "+individual_obj.work_place+"  To Name = "+name+" Gender = "+gender+" DOB = "+date_of_birth+" M State = "+marital_status+" State = "+state+" Address  = "+address+" Phone = "+phone+" Email = "+email+" Occupation = "+occupation+" Employement Status  = "+employment_status+" Work Place = "+work_place, generated_by= user)

				 
				individual_obj.name = name
				individual_obj.gender = gender
				individual_obj.date_of_birth = date_of_birth
				individual_obj.marital_status = marital_status
				individual_obj.state = state
				individual_obj.address = address
				individual_obj.phone = phone
				individual_obj.email = email
				individual_obj.occupation = occupation
				individual_obj.employment_status = employment_status
				individual_obj.work_place= work_place

				notification.save()

				individual_obj.save()

				

				messages.success(req, "Individual record Updated Successfuly ", extra_tags= "record_updated")
		 
				return HttpResponseRedirect('/tin/edit-individual/'+str(individual_obj.id))

			else:
				messages.success(req, "Password or user name is wrong ", extra_tags= "wrong_pass") 
				return render(req, 'edit_individual_record.html')

		else: 
			messages.success(req, "User Record Created", extra_tags= "wrong_data") 
			return render(req, 'edit_individual_record.html')

		
	except Exception as e:
		print(e)
		messages.success(req, "User Record Created", extra_tags= "wrong_data")
		return render(req, 'edit_individual_record.html')


def edit_company(req, company_id):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator" or "TIN User":

			if company_id != "":

				try:
					company_obj =  Company.objects.get(id = company_id)

					# work_places  = Company.objects.all()

					return render(req, 'edit_company_record.html', {'company_obj':company_obj} )
					
				except Individual.DoesNotExist:
					return HttpResponseRedirect('/tin/companies/')
 
 
			else:
				 
				return HttpResponseRedirect('/tin/companies/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def update_company(req):

	 
	try:		
		form = EditCompanyForm(req.POST)

		if form.is_valid():
			
			paswd = form.cleaned_data.get("password")
			user_id = req.session['user_id']
			user = User.objects.get(id = user_id)

			if user.password == crypt(paswd, user.password):

				company_id = req.POST.get("id")
				tin = req.POST.get("tin")
				institution = form.cleaned_data.get("institution")
				local_government = form.cleaned_data.get("local_government")
				bussiness_status = form.cleaned_data.get("bussiness_status")
				bussiness_class = form.cleaned_data.get("bussiness_class")
				registration_number = form.cleaned_data.get("registration_number")
				bussiness_ownership_type = form.cleaned_data.get("bussiness_ownership_type")
				bussiness_name = form.cleaned_data.get("bussiness_name")
				bussiness_owner = form.cleaned_data.get("bussiness_owner")
				bussiness_address = form.cleaned_data.get("bussiness_address")
				phone_number = form.cleaned_data.get("phone_number")
				email = form.cleaned_data.get("email")
				 
				institution_type_id = form.cleaned_data.get("institution_type")
				institution_category_id = form.cleaned_data.get("institution_category")


				
				company_obj = Company.objects.get(tin = tin)

				institution_type_obj = InstitutionType.objects.get(id = institution_type_id)
				institution_category_obj = InstitutionCategory.objects.get(id = institution_category_id)

				notification = Notification(notification_for= "Company", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" Edited Comany record ID:"+str(company_obj.id)+
					" From Institution = "+company_obj.institution+" LGV = "+company_obj.local_government+" Buss State = "+company_obj.bussiness_status+" Buss Class = "+company_obj.bussiness_class+
					" Reg Number = "+company_obj.registration_number+" Buss ownershiptype = "+company_obj.bussiness_ownership_type+" Bussiness Name = "+company_obj.bussiness_name+" Buss Owner = "+company_obj.bussiness_owner+
					" Buss Address = "+company_obj.bussiness_address+" Phone = "+company_obj.phone_number+" Email= "+company_obj.email+
					" Institution Type = "+company_obj.institution_type.type_name+" Institution Category = "+company_obj.institution_category.category_name+
					" To Institution = "+institution+" LGV = "+local_government+" Buss State = "+bussiness_status+" Buss Class = "+bussiness_class+
					" Reg Number = "+registration_number+" Buss ownershiptype = "+bussiness_ownership_type+" Bussiness Name = "+bussiness_name+" Buss Owner = "+bussiness_owner+
					" Buss Address = "+bussiness_address+" Phone = "+phone_number+" Email= "+email+
					" Institution Type = "+str(institution_type_obj.id)+" Institution Category = "+str(institution_category_obj.id), generated_by= user)

				 
				company_obj.institution = institution
				company_obj.local_government = local_government
				 
				company_obj.institution_type = institution_type_obj
				company_obj.institution_category = institution_category_obj
				company_obj.bussiness_status = bussiness_status
				company_obj.bussiness_class = bussiness_class
				company_obj.registration_number = registration_number
				company_obj.bussiness_ownership_type = bussiness_ownership_type
				company_obj.bussiness_name = bussiness_name
				company_obj.bussiness_owner = bussiness_owner
				company_obj.bussiness_address = bussiness_address
				company_obj.phone_number = phone_number
				company_obj.email = email
				 
				

				
				notification.save()
				company_obj.save()

				messages.success(req, "Individual record Updated Successfuly ", extra_tags= "record_updated")
		 
				return HttpResponseRedirect('/tin/edit-company/'+str(company_obj.id))

			else:
				messages.success(req, "Password or user name is wrong ", extra_tags= "wrong_pass") 
				return render(req, 'edit_company_record.html')

		else: 
			print(form.errors)
			messages.success(req, "User Record Created", extra_tags= "wrong_data") 
			return render(req, 'edit_company_record.html')

		
	except Exception as e:
		print(e)
		messages.success(req, "User Record Created", extra_tags= "wrong_data")
		return render(req, 'edit_company_record.html')



 

def individuals(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator' or 'TIN User':
			 
			individuals = Individual.objects.all()			
		 
			return render(req, 'individuals.html', {"individuals":individuals})				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')

def add_individual(req):
	user_access_level  = req.session.get("access_level")
	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator" or "TIN User":		 

			if req.method == "GET":
				LGAs = LocalGovArea.objects.all()
				work_places = Company.objects.all()
		
				return render(req, 'add_individual.html', {"LGAs":LGAs, "work_places":work_places})
				
			else:
				 
				return render(req, 'add_individual.html')
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def i_data_preview_before_saving(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator" or "TIN User":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/tin/add-individual/')

			elif req.method == "POST" and req.POST:				 
				
				form = IndividualForm(req.POST)

				if form.is_valid():
					
				
					try:			
						new_tin = generate_tin(req)
						if len(new_tin) == 10:					
							tin_obj = AssignedTin.objects.filter(tin = new_tin)

							while tin_obj.exists():
								new_tin = generate_tin(req)
								tin_obj = AssignedTin.objects.filter(tin = new_tin)


							title = req.POST.get("title")
							name = form.cleaned_data.get("name")
							gender = form.cleaned_data.get("gender")
							date_of_birth = form.cleaned_data.get("date_of_birth")
							marital_status = form.cleaned_data.get("marital_status")
							state = form.cleaned_data.get("state")
							address = form.cleaned_data.get("address")
							phone = form.cleaned_data.get("phone")
							email = form.cleaned_data.get("email")
							occupation = form.cleaned_data.get("occupation")
							employment_status = form.cleaned_data.get("employment_status")
							work_place = form.cleaned_data.get("work_place")

							data_context = {"tin":new_tin, 'name':title+" "+name, 'gender':gender, 'date_of_birth':date_of_birth, 'marital_status':marital_status, 'state':state, 'address':address, 'phone':phone, 'email':email, 'occupation':occupation, 'employment_status':employment_status, 'work_place':work_place }
							
							messages.success(req, " Record Preview ",  extra_tags = 'i_data_preview data' )
							return render(req, 'add_individual.html', data_context)

						else:
							print("tin cant be generated")	
							return HttpResponseRedirect('/tin/add-individual/')
							 		
					except Exception as e:
						print(e)			 
						messages.info(req, "uncaught Exception")
						return HttpResponseRedirect('/tin/add-individual/')	

					except User.DoesNotExist:					 
						messages.info(req, "uncaught Exception")
						return HttpResponseRedirect('/tin/add-individual/')	

					except Office.DoesNotExist:					 
						messages.info(req, "uncaught Exception")
						return HttpResponseRedirect('/tin/add-individual/')		
					
				else:
					print(form.errors)
					messages.info(req, "invalid form fields")
					return HttpResponseRedirect('/tin/add-individual/')

 

				
			else:
				
				return HttpResponseRedirect('/tin/add-individual/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')




def save_individual(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator" or "TIN User":	

			if req.method == "POST" and req.POST: 		 
				

					signed_in_user_id = req.session.get("user_id")
					try:		
						
						tin = req.POST.get("tin")
						name = req.POST.get("name")
						gender = req.POST.get("gender")
						date_of_birth = req.POST.get("date_of_birth")
						marital_status = req.POST.get("marital_status")
						state = req.POST.get("state")
						address = req.POST.get("address")
						phone = req.POST.get("phone")
						email = req.POST.get("email")
						occupation = req.POST.get("occupation")
						employment_status = req.POST.get("employment_status")
						work_place = req.POST.get("work_place")

						staff_obj = User.objects.get(id = signed_in_user_id)
						
						
						check_tin =  AssignedTin.objects.filter(tin = tin)

						req.session['temp_sess_individual_name'] =name
						req.session['temp_sess_individual_tin'] = tin

						if check_tin.exists():
							messages.success(req, "Individual record already created", extra_tags= "record_already_created")
							return HttpResponseRedirect('/tin/add-individual/')
						else:
							tin_obj = AssignedTin.objects.create(tin = tin,  tin_for = "Individual")
							individual_obj = Individual.objects.create(tin = tin_obj, name = name, gender = gender, date_of_birth = date_of_birth, marital_status = marital_status, state = state, address = address, phone = phone, email = email, occupation = occupation, employment_status = employment_status, work_place= work_place, staff = staff_obj)
							
							req.session['temp_sess_individual_tin_id'] = individual_obj.id
							messages.success(req, "User Record Created", extra_tags= "record_created")
							return HttpResponseRedirect('/tin/add-individual/')

						
					except Exception as e:
						print(e)
						return HttpResponseRedirect('/tin/add-individual/')
								
						 
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

 
		 
def add_company(req):
	user_access_level  = req.session.get("access_level")
	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator" or "TIN User":		 

			if req.method == "GET":
				institution_categories = InstitutionCategory.objects.all()
				institution_types = InstitutionType.objects.all()
				LGAs = LocalGovArea.objects.all()
				
				return render(req, 'add_company.html', {"LGAs":LGAs, "institution_types":institution_types, "institution_categories":institution_categories })
			
			else:
				 
				return render(req, 'add_company.html')
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')




@csrf_exempt
def save_snap(req):
	 
	img_data_string = req.POST['base64image']	 
	new_data_img_str = img_data_string.replace("data:image/jpeg;base64,", "")

	name = req.session.get("temp_sess_individual_name")
	tin = req.session.get("temp_sess_individual_tin")	 

	try:

		if 'temp_sess_individual_name' in req.session  and ('temp_sess_individual_tin' in req.session):
			new_image = open("tin/static/images/individual_images/"+name.upper()+":"+tin+".jpeg", "wb")
			new_image.write(base64.b64decode(new_data_img_str))
			new_image.close()

			user = Individual.objects.get(id = req.session['temp_sess_individual_tin_id'])
			user.passport_pic_url = "/static/images/individual_images/"+name.upper()+":"+tin+".jpeg"
			user.save()

			del req.session['temp_sess_individual_name']
			del req.session['temp_sess_individual_tin']
			del req.session['temp_sess_individual_tin_id']

			return JsonResponse({"res":"success"})
		else:
			return JsonResponse({"res":"fail"})

 
	except Exception as e:
	    return JsonResponse({"res":"fail"})
 

 
 


# /home/hakim-developer/Pictures/sulix wedding/IMG-20150731-WA0003.jpg
