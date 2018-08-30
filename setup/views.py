from django.shortcuts import render 
from django.db import IntegrityError
from django.contrib import messages
from django.http import JsonResponse
import os
from django.http import HttpResponseRedirect

# import bcrypt
from pbkdf2 import crypt

from setup.models import User, Office, LocalGovArea, StateCode, Charge, InstitutionCategory, InstitutionType, ChargesOthers, Notification
from setup.controllers.dashboard import dashboard

from setup.forms import LoginForm, UserForm, LocalGovAreaForm, OfficeForm, EditInstitutionForm, EditUserForm, EditOfficeForm, EditStateCodeForm, EditOtherChargeForm, EditLGAForm, ChargeForm, PasswordTextForm, InstitutionCategoryForm, InstitutionTypeForm, OtherChargeForm


def login(req):
	if req.method == "GET" and   ('user_id' not in req.session):
		# load login form 
		return render(req, 'login.html')

	elif ('user_id' in req.session) and ('access_level' in req.session):
		# user is already logged in
		return dashboard(req)	 
		
		
	elif req.method == "POST" and req.POST:
		# user is logining in

		form = LoginForm(req.POST)
		if form.is_valid():			 
			
			# field not validated
			user_name = req.POST.get("user_name")
			paswd = form.cleaned_data.get('password')

			try:				 

				user = User.objects.get(user_name = user_name)

				if user.is_active:
					if not user.password == "password":

					 



						# if bcrypt.checkpw(paswd.encode('utf-8'), user.password.encode('utf-8')):
						if user.password == crypt(paswd, user.password):
							
							req.session['office_id'] = user.office.id
							req.session['access_level'] = user.access_level
							req.session['name'] = user.full_name
							req.session['user_id'] = user.id
							user.is_onLine = True

							user.save()

							return dashboard(req)	
						else:
							messages.info(req, "Password or user name is wrong")
							return render(req, 'login.html')


					else:
						req.session['temp_user_id'] = user.id
						# req.session['temp_user_name'] = user.user_name
						messages.info(req, "Please change your password to continue", extra_tags = "change_password")
						return render(req, 'dashboard.html')
				else:
					messages.info(req, "This account is not active")
					return render(req, 'login.html')					
			 					
			except User.DoesNotExist:
				# user does not exist
				messages.info(req, "Password or user name is wrong")
				return render(req, 'login.html')						
		else:
			print(form.errors)

			messages.warning(req, "Please input correct data in fields")
			return render(req, 'login.html')

	else:
		return render(req, 'login.html')

def create_password(req):

	if 'temp_user_id' in req.session:

		if req.method == "POST" and req.POST:
			# user is logining in

			form = PasswordTextForm(req.POST)
			if form.is_valid():		
				
				paswd = req.POST.get("password")
				user_id = req.session['temp_user_id']

				try:
					if paswd == "password":
						messages.info(req, "Please change your password to continue", extra_tags = "change_password")
						return render(req, 'dashboard.html')
					else:

						user = User.objects.get(pk = user_id)

						user.password  = crypt(paswd)

						req.session['office_id'] = user.office.id
						req.session['access_level'] = user.access_level
						req.session['name'] = user.full_name
						req.session['user_id'] = user.id
						user.is_onLine = True
						user.save()

						del req.session['temp_user_id']

						messages.warning(req, "", extra_tags="password_created")

						return dashboard(req)

				except Exception as e:
					raise e

							
			else:
				return render(req, 'login.html')
	else:
		return render(req, 'login.html')
 		
	 

def users(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			users = User.objects.all()
			
			return render(req, 'users.html', {"users":users})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')



 

def add_user(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":
			offices = Office.objects.all()	 

			if req.method == "GET":
				offices = Office.objects.all()	
				return render(req, 'add_user.html', {"offices":offices})

			elif req.method == "POST" and req.POST:
				form  = UserForm(req.POST)
				if form.is_valid():

					try:
						 
						user = form.save(commit = False)
						office_id = req.POST.get("office_id")

						office = Office.objects.get(id = office_id)
						 
						user.office =office							 
						user.save()

						messages.success(req, "User Created", extra_tags = "record_created")
						return HttpResponseRedirect('/set-up/add-user/')

	  

					except Exception as e:
						return HttpResponseRedirect('/set-up/add-user/') 
				else:
					if form['user_name'].errors:
						messages.success(req, "LGA already exist", extra_tags = "record_already_created")
						return HttpResponseRedirect('/set-up/add-user/') 

					else:
						messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
						return HttpResponseRedirect('/set-up/add-user/')
			 

		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-user')			 
		
	else:				 
		return render(req, 'login.html')
	
def offices(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':

			offices = Office.objects.all()	 

			return render(req, 'offices.html', {"offices":offices})				
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')


def add_office(req): 
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				return render(req, 'add_office.html')

			elif req.method == "POST" and req.POST:				 
				form = OfficeForm(req.POST)

				if form.is_valid():
				
					try:
						office_name = form.cleaned_data.get("office_name")
						 
						Office.objects.create(office_name = office_name) 
						messages.success(req, "Office Created", extra_tags = "record_created")
						return HttpResponseRedirect('/set-up/add-office/')
						

					except IntegrityError as e:
						
						messages.success(req, "Office already exist", extra_tags = "record_already_created")
						return HttpResponseRedirect('/set-up/add-office/') 

					except Exception as e:
						return HttpResponseRedirect('/set-up/add-office/') 
				else:
					 
					messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/add-office/')
			 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-office')			 
		
	else:				 
		return render(req, 'login.html')
def add_lga(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				return render(req, 'add_LGA.html')

			elif req.method == "POST" and req.POST:				 
				form = LocalGovAreaForm(req.POST)

				if form.is_valid():
				
					try:
						lga_name = form.cleaned_data.get("local_government_name")
						lga_code = form.cleaned_data.get("local_government_code")
						LocalGovArea.objects.create(local_government_name = lga_name, local_government_code = lga_code)
 
						messages.success(req, "LGA Created", extra_tags = "record_created")
						return HttpResponseRedirect('/set-up/add-lga/')
						

					except IntegrityError as e:
						
						messages.success(req, "LGA already exist", extra_tags = "record_already_created")
						return HttpResponseRedirect('/set-up/add-lga/') 

					except Exception as e:
						return HttpResponseRedirect('/set-up/add-lga/') 
				else:
					 
					messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/add-lga/')
			 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-lgas')			 
		
	else:				 
		return render(req, 'login.html')
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				
				return render(req, 'add_office.html')

			elif req.method == "POST" and req.POST:				 
					form = OfficeForm(req.POST)

					if form.is_valid():
						

						try:
							office_name = form.cleaned_data.get("office_name")
							office_obj, created =  Office.objects.get_or_create(office_name = office_name)

							if created:
								 
								messages.success(req, "Office Created", extra_tags = "office_added")
								return HttpResponseRedirect('/set-up/add-office/')
							else:
								 
								messages.success(req, "Office already exist", extra_tags ="office_already_added")
								return HttpResponseRedirect('/set-up/add-office/')

						except Exception as e:
							print(e)
							 
							messages.info(req, "uncaught Exception")
							return HttpResponseRedirect('/set-up/add-office/')
					else:
						messages.success(req, "Invalid Data", extra_tags = "invalid_data")
						return HttpResponseRedirect('/set-up/add-office/')
				
			else:
				HttpResponseRedirect('/set-up/add-office/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
			
	else:
		messages.info(req, "singn in")		 
		return HttpResponseRedirect('/login/')


def lgas(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':
			 
			lgas = LocalGovArea.objects.all()	

			try:
				state_code_obj = StateCode.objects.get(id = 1)
				state_code = state_code_obj.state_code
				state_code_value = state_code_obj.state_code
				return render(req, 'lga.html', { "lgas":lgas, "state_code":state_code, "state_code_value":state_code_value})
					
			except StateCode.DoesNotExist:
				 
				state_code_value = "#"
				return render(req, 'lga.html', { "lgas":lgas, "state_code_value":"#"})
									
			 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")
			return render(req, 'login.html')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')


	


	
def add_lga(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				return render(req, 'add_LGA.html')

			elif req.method == "POST" and req.POST:				 
				form = LocalGovAreaForm(req.POST)

				if form.is_valid():
				
					try:
						lga_name = form.cleaned_data.get("local_government_name")
						lga_code = form.cleaned_data.get("local_government_code")
						LocalGovArea.objects.create(local_government_name = lga_name, local_government_code = lga_code)
 
						messages.success(req, "LGA Created", extra_tags = "record_created")
						return HttpResponseRedirect('/set-up/add-lga/')
						

					except IntegrityError as e:
						
						messages.success(req, "LGA already exist", extra_tags = "record_already_created")
						return HttpResponseRedirect('/set-up/add-lga/') 

					except Exception as e:
						return HttpResponseRedirect('/set-up/add-lga/') 
				else:
					 
					messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/add-lga/')
			 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-lgas')			 
		
	else:				 
		return render(req, 'login.html')


def add_state_code(req): 
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				 			
				return HttpResponseRedirect('/set-up/lgas')

			elif req.method == "POST" and req.POST:				 
				form = EditStateCodeForm(req.POST)

				if form.is_valid():
					user_id = req.session['user_id']
				
					try:						
						
						user = User.objects.get(id = user_id)
						state_code = form.cleaned_data.get("state_code")
						paswd = form.cleaned_data.get("password")

						if user.password == crypt(paswd, user.password):
						
							

							if (len(state_code) == 2):

								try:
									state_code_obj = StateCode.objects.get(id = 1)
									

									notification = Notification(notification_for= "StateCode", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited State Code record ID:"+str(state_code_obj.id)+" From LGA Name = "+state_code_obj.state_code+"  To State Code name = "+state_code, generated_by= user)

									state_code_obj.state_code = state_code

									notification.save()
									state_code_obj.save()			
									 
									messages.info(req, "record updated", extra_tags = "record_updated")
									return HttpResponseRedirect('/set-up/lgas/')

								except StateCode.DoesNotExist:
									StateCode.objects.create(state_code = state_code)

									messages.info(req, "record updated", extra_tags = "record_updated")
									return HttpResponseRedirect('/set-up/lgas/')
									
							else:
								messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
								return HttpResponseRedirect('/set-up/lgas')

						else:
							messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
							return HttpResponseRedirect('/set-up/lgas')
					 
 
					except User.DoesNotExist: 
						return HttpResponseRedirect('/set-up/login')						
						
 
				 
				else:					 
					messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/lgas')

		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/lgas')

		 
def charges(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':
			 
			charges = Charge.objects.all()
		 
			return render(req, 'charges.html', {"charges":charges})				
			 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/charges')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')

def other_charges(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):


		if user_access_level == 'Super Administrator':
			 
			other_charges = ChargesOthers.objects.all()
		 
			return render(req, 'other_charges.html', {"other_charges":other_charges})				
			 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/other-charges')
		
	else:
		messages.info(req, "Sign in Please")
		return render(req, 'login.html')


def add_charge(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":								
				return render(req, 'add_charge.html')

			elif req.method == "POST" and req.POST:				 
				form = ChargeForm(req.POST)

				if form.is_valid():				 

					try:
						charge_type = form.cleaned_data.get("options")
						vehicle_type = form.cleaned_data.get("vehicle_type")
						particulars = form.cleaned_data.get("particulars")
						amount = form.cleaned_data.get("amount")						 

						charge_obj = Charge.objects.get(options = charge_type, vehicle_type = vehicle_type, particulars = particulars)
						messages.success(req, "Charge exist", extra_tags = "record_exist")
						return HttpResponseRedirect('/set-up/add-charge/')
						
					except Charge.DoesNotExist as e:
						Charge.objects.create(options = charge_type, vehicle_type = vehicle_type, particulars = particulars, amount = amount)
						messages.success(req, "Charge Created", extra_tags = "record_created")
						return HttpResponseRedirect('/set-up/add-charge/')
						 
					 
				else:
					print(form.errors)
					messages.info(req, "Record exist", extra_tags="wrong_data")
					return HttpResponseRedirect('/set-up/add-charge/')	
		
	else:
		messages.info(req, "Access Denied", extra_tags = "access_denied")
		return HttpResponseRedirect('/set-up/add-charge')
	 		 
	
def edit_charge(req):
	 

	if 'user_id' in req.session  and ('access_level' in req.session):		
 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/set-up/charges')

		elif req.method == "POST" and req.POST:				 
			form = PasswordTextForm(req.POST) 

			if form.is_valid():
				charge_id = req.POST.get("charge_id")
				charge_type = req.POST.get("charge_type")
				vehicle_type = req.POST.get("vehicle_type")
				particulars = req.POST.get("particulars")
				amount = req.POST.get("amount")
				paswd = form.cleaned_data.get("password") 


				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):

						charge_obj = Charge.objects.get(id = charge_id)
						notification = Notification(notification_for= "Charge", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited Charge record ID:"+str(charge_obj.id)+" From Charge Type = "+ charge_obj.options+" , Vehicle Type = "+charge_obj.vehicle_type+" , Particulars = "+charge_obj.particulars+" , Amount = "+str(charge_obj.amount)+	" To Charge Type = "+charge_type+" , Vehicle Type = "+vehicle_type+" , Particulars = "+particulars+" , Amount = "+amount, generated_by= user)

						charge_obj.options = charge_type
						charge_obj.vehicle_type = vehicle_type
						charge_obj.particulars = particulars
						charge_obj.amount = amount

						
						notification.save()
						charge_obj.save()

						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/set-up/charges')


					else:
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/charges')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/set-up/login')

				except IntegrityError as e:
					messages.success(req, "Charge already exist", extra_tags = "record_already_created")
					return HttpResponseRedirect('/set-up/charges/') 

					 


			else:
				 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/charges')
	else:
		 		 
		return render(req, 'login.html')
 
def edit_other_charge(req):
	 

	if 'user_id' in req.session  and ('access_level' in req.session):		
 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/set-up/charges')

		elif req.method == "POST" and req.POST:				 
			form = EditOtherChargeForm(req.POST) 

			if form.is_valid():
				charge_id = req.POST.get("charge_id")
				 
				particulars = req.POST.get("particulars")
				amount = form.cleaned_data.get("amount")
				paswd = form.cleaned_data.get("password")

				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):

						charge_obj = ChargesOthers.objects.get(id = charge_id)
						notification = Notification(notification_for= "ChargesOthers", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited Other Charge record ID:"+str(charge_obj.id)+" From Charge Particulars = "+ charge_obj.particulars+" , Amount = "+str(charge_obj.amount)+" To Particulars = "+particulars+" , Amount = "+str(amount), generated_by= user)
 
						charge_obj.particulars = particulars
						charge_obj.amount = amount

						
						notification.save()
						charge_obj.save()

						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/set-up/other-charges')


					else:
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/other-charges')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/set-up/login')

				except IntegrityError as e:
					messages.success(req, "Charge already exist", extra_tags = "record_already_created")
					return HttpResponseRedirect('/set-up/other-charges/') 

					 

			else:
				 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/other-charges')
	else:
		 		 
		return render(req, 'login.html')

def toggle_charge_state(req):
	user_access_level  = req.session.get("access_level")
	
	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == "Super Administrator": 

			if req.method == "GET":				 			
				return HttpResponseRedirect('/set-up/charges')

			elif req.method == "POST" and req.POST:

				form = PasswordTextForm(req.POST)
				if form.is_valid():
					charge_id = req.POST.get("charge_id")				 
					paswd = form.cleaned_data.get("password") 
	 
					try:

						user_id = req.session['user_id']
						user = User.objects.get(id = user_id)



						if user.password == crypt(paswd, user.password):

							charge_obj = Charge.objects.get(id = charge_id)

							if charge_obj.is_active:

								old_state = "Active"

								notification =  Notification(notification_for= "Charge", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Changed Charge state of record ID:"+str(charge_obj.id)+" From Status = "+ str(charge_obj.is_active)+"  To Charge Status = "+old_state, generated_by= user)
								charge_obj.is_active = False
								  
								
								notification.save()
								charge_obj.save()


								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/charges')

							else:
								old_state = "Inactive"								

								notification = Notification(notification_for= "Charge", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Changed Charge state of record ID:"+str(charge_obj.id)+" From Status = "+ str(charge_obj.is_active)+"  To Charge Status = "+old_state, generated_by= user)
								charge_obj.is_active = True

								 							
								notification.save()
								charge_obj.save()
	 
								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/charges')
								


						else:
							 
							messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
							return HttpResponseRedirect('/set-up/charges')

					except User.DoesNotExist: 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/login')

					 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-charge')


	else:
		return render(req, 'login.html')

def add_other_charge(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
								
				return render(req, 'add_other_charge.html')

			elif req.method == "POST" and req.POST:				 
				form = OtherChargeForm(req.POST)

				if form.is_valid():				 

					try:
						particulars = form.cleaned_data.get("particulars")
						amount = form.cleaned_data.get("amount") 

						ChargesOthers.objects.create(particulars = particulars, amount = amount)

						messages.success(req, "Other Charge Created", extra_tags = "record_created")				 
						return HttpResponseRedirect('/set-up/add-other-charge/')

					except Exception as e:
						print(e)

					
				else:
					 
					if form['particulars'].errors:

						messages.info(req, "Change exist", extra_tags="record_already_created")
						return HttpResponseRedirect('/set-up/add-other-charge/')

					elif form['amount'].errors:						 
						messages.info(req, "amount value data", extra_tags="wrong_data")
						return HttpResponseRedirect('/set-up/add-other-charge/')
 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-charge')
		
	else:		 	 
		return render(req, 'login.html')


def toggle_other_charge_state(req):

	user_access_level  = req.session.get("access_level")
	
	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == "Super Administrator": 

			if req.method == "GET":				 			
				return HttpResponseRedirect('/set-up/other-charges')

			elif req.method == "POST" and req.POST:

				form = PasswordTextForm(req.POST)
				if form.is_valid():
					charge_id = req.POST.get("charge_id")				 
					paswd = form.cleaned_data.get("password") 
					print(charge_id)
	 
					try:

						user_id = req.session['user_id']
						user = User.objects.get(id = user_id)



						if user.password == crypt(paswd, user.password):

							charge_obj = ChargesOthers.objects.get(id = charge_id)

							if charge_obj.is_active:
								
								old_state = "Active"

								notification = Notification(notification_for= "Other Charge", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Changed Charge state of record ID:"+str(charge_obj.id)+" From Status = "+ str(charge_obj.is_active)+"  To Charge Status = "+old_state, generated_by= user)
								
								charge_obj.is_active = False
								 
								
								notification.save()
								charge_obj.save()


								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/other-charges')

							else:
								

								old_state = "Inactive"

								notification = Notification(notification_for= "Other Charge", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Changed Charge state of record ID:"+str(charge_obj.id)+" From Status = "+ str(charge_obj.is_active)+"  To Charge Status = "+old_state, generated_by= user)
								
								charge_obj.is_active = True
								
								 
								
								notification.save()
								charge_obj.save()
	 
								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/other-charges')
								


						else:

							messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
							return HttpResponseRedirect('/set-up/other-charges')

					except User.DoesNotExist: 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/login')

					 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/other-charges')


	else:
		return render(req, 'login.html')

def institution_categories(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			institution_categories = InstitutionCategory.objects.all()
			
			return render(req, 'institution_categories.html', {"institution_categories":institution_categories})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Access Denied", extra_tags = "access_denied")
		


def add_institution_category(req):
 
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":

				return render(req, 'add_institution_category.html')

			elif req.method == "POST" and req.POST:	
				 
				form = InstitutionCategoryForm(req.POST)

				if form.is_valid():
				
					try:
						category_name = form.cleaned_data.get("category_name")		 
						 
						InstitutionCategory.objects.create(category_name = category_name)
						messages.success(req, "Office Created", extra_tags = "record_created")
						return HttpResponseRedirect('/set-up/add-institution-category/')
				 
					except Exception as e:
						
						return HttpResponseRedirect('/set-up/add-institution-category/') 
				else:

					if form['category_name'].errors:
						messages.success(req, "Institution Category already exist", extra_tags = "record_already_created")
						return HttpResponseRedirect('/set-up/add-institution-category/')
										
					else:
						messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
						return HttpResponseRedirect('/set-up/add-institution-category/')
			 
		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-institution-category/')			 
		
	else:				 
		return render(req, 'login.html')

 

def add_institution_type(req):
 
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":

				return render(req, 'add_institution_type.html')

			elif req.method == "POST" and req.POST:
				form = InstitutionTypeForm(req.POST)
				if form.is_valid():
 					type_name = form.cleaned_data.get("type_name")


 					try:
 						InstitutionType.objects.create(type_name = type_name)
 						messages.info(req, "Institution Type created", extra_tags = "record_created")
 						return HttpResponseRedirect('/set-up/add-institution-type/')
 					except Exception as e:
 						return HttpResponseRedirect('/set-up/add-institution-type/') 

				else:
					if form['type_name'].errors:
						messages.success(req, "Institution Category already exist", extra_tags = "record_already_created")
						return HttpResponseRedirect('/set-up/add-institution-type/')

		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/add-institution-type/')
	else:				 
		return render(req, 'login.html')

 				

def institution_types(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'Super Administrator':			 
			institution_types = InstitutionType.objects.all()
			
			return render(req, 'institution_types.html', {"institution_types":institution_types})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			 
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')



	
 
 
def edit_user(req, user_id):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":

			try:
				user = User.objects.get(id = user_id)
				offices = User.objects.all()
				return render(req, 'edit_user.html', {"user":user, 'offices':offices})

			except User.DoesNotExist as e:
				messages.info(req, "Wrong data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/users')			

		else:
 			messages.info(req, "Access Denied", extra_tags = "access_denied")
 			return HttpResponseRedirect('/set-up/other-charges')
	else:
 		return render(req, 'login.html')



def edit_user_(req):
	 

	if 'user_id' in req.session  and ('access_level' in req.session): 	 

		

		if req.method == "POST" and req.POST:

			form = EditUserForm(req.POST)


			if form.is_valid():
				 
				user_to_edit_id = req.POST.get("user_id")

				office_id = req.POST.get("office_id")				 
				 
				full_name = form.cleaned_data.get("full_name")
				user_name = form.cleaned_data.get("user_name")
				department = form.cleaned_data.get("department")
				access_level = form.cleaned_data.get("access_level")
			 
				paswd = form.cleaned_data.get("password")

				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					office_obj = Office.objects.get(id = office_id)

					if user.password == crypt(paswd, user.password):

						user_obj = User.objects.get(id = user_to_edit_id)

						notification = Notification(notification_for= "User", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited user record ID:"+str(user_obj.id)+" From Name = "+ user_obj.full_name+" , Email = "+ user_obj.user_name+", Department  = "+ user_obj.department+"Acces Level = "+ user_obj.access_level+"Office  = "+ str(user_obj.office.id)+" To Name = "+ full_name+" , Office = "+ str(office_id)+" , Email = "+ user_name+
							", Department  = "+department+"Acces Level = "+ access_level, generated_by= user)
						

 
						user_obj.full_name = full_name
						user_obj.user_name = user_name
						user_obj.department = department
						user_obj.access_level = access_level
						user_obj.office = office_obj
						 
						
						notification.save()
						user_obj.save()

						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/set-up/users') 
					else:

						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return render(req ,"edit_user.html")

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/set-up/login')
				except Office.DoesNotExist:
					messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/edit-user')

				except IntegrityError as e:
					 
					messages.success(req, "Email Already Exist already exist", extra_tags = "record_already_created")
					return HttpResponseRedirect('/set-up/users/') 
 	 

			else:
				 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/edit-user')
		else:
			 
			messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
			return render(req ,"edit_user.html")
	else:
		 		 
		return render(req, 'login.html')

def edit_office(req):
	 

	if 'user_id' in req.session  and ('access_level' in req.session): 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/set-up/offices')

		elif req.method == "POST" and req.POST:				 
			form = EditOfficeForm(req.POST) 

			if form.is_valid():
				office_id = req.POST.get("office_id")				 
				 
				office_name = form.cleaned_data.get("office_name")
				paswd = form.cleaned_data.get("password")

				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):

						office_obj = Office.objects.get(id = office_id)
						notification = Notification(notification_for= "Office", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited Office record ID:"+str(office_obj.id)+" From Office Name = "+ office_obj.office_name+", To Particulars = "+office_name, generated_by= user)

						office_obj.office_name = office_name
						 
						
						notification.save()
						office_obj.save()

						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/set-up/offices')
 
					else:
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/offices')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/set-up/login')

				except IntegrityError as e:
				 
					messages.success(req, "Charge already exist", extra_tags = "record_already_created")
					return HttpResponseRedirect('/set-up/offices/') 

					 

			else:
			 	 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/offices')
	else:
		 		 
		return render(req, 'login.html')



def edit_institution_category(req):	 

	if 'user_id' in req.session  and ('access_level' in req.session): 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/set-up/institution-categories/')

		elif req.method == "POST" and req.POST:				 
			form = EditInstitutionForm(req.POST) 

			if form.is_valid():
				category_id = req.POST.get("category_id")				 
				 
				category_name = form.cleaned_data.get("institution_text")
				paswd = form.cleaned_data.get("password")

				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):

						institution_obj = InstitutionCategory.objects.get(id = category_id)

						notification = Notification(notification_for= "Institution Category", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited Institution Category record ID:"+str(institution_obj.id)+" From Institution Name = "+ institution_obj.category_name+", To Institution Name = "+category_name, generated_by= user)

						 
						institution_obj.category_name = category_name
						 
						
						notification.save()
						institution_obj.save()
						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/set-up/institution-categories/')
 
					else:
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/institution-categories/')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/set-up/login')

				except IntegrityError as e:
				 
					messages.success(req, "Charge already exist", extra_tags = "record_already_created")
					return HttpResponseRedirect('/set-up/institution-categories/') 

					 

			else:
			 	 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/institution-categories/')
	else:
		 		 
		return render(req, 'login.html')
 

def edit_institution_type(req):	 

	if 'user_id' in req.session  and ('access_level' in req.session): 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/set-up/institution-types/')

		elif req.method == "POST" and req.POST:				 
			form = EditInstitutionForm(req.POST) 

			if form.is_valid():
				category_id = req.POST.get("category_id")				 
				 
				type_name = form.cleaned_data.get("institution_text")
				paswd = form.cleaned_data.get("password")

				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):

						institution_obj = InstitutionType.objects.get(id = category_id)

						notification = Notification(notification_for= "Institution Type", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited Institution Category record ID:"+str(institution_obj.id)+" From Institution Type Name = "+ institution_obj.type_name+", To Institution Type Name = "+type_name, generated_by= user)

						 
						institution_obj.type_name = type_name
						 
						
						
						notification.save()
						institution_obj.save()
						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/set-up/institution-types/')
 
					else:
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/institution-types/')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/set-up/login')

				except IntegrityError as e:
				 
					messages.success(req, "Charge already exist", extra_tags = "record_already_created")
					return HttpResponseRedirect('/set-up/institution-types/')
			else:
			 	 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/institution-types/')
	else:
		 		 
		return render(req, 'login.html')

def toggle_user_state(req):
	 
	user_access_level  = req.session.get("access_level")
	
	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == "Super Administrator": 

			if req.method == "GET":				 			
				return HttpResponseRedirect('/set-up/users')

			elif req.method == "POST" and req.POST:

				form = PasswordTextForm(req.POST)
				if form.is_valid():
					user_to_edit_id = req.POST.get("user_id")				 
					paswd = form.cleaned_data.get("password") 
	 
					try:
						 
						user_id = req.session['user_id']
						user = User.objects.get(id = user_id)



						if user.password == crypt(paswd, user.password):

							user_obj = User.objects.get(id = user_to_edit_id)
							 
							if user_obj.is_active:
								old_state = "Active"
								notification = Notification(notification_for= "User", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" User state of record ID:"+str(user_obj.id)+" From Status = "+ str(user_obj.is_active)+"  To User Status = "+old_state, generated_by= user)
								user_obj.is_active = False
								
								 
								
								
								notification.save()
								user_obj.save()


								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/users')

							else:
								old_state = "Inactive"
								notification = Notification(notification_for= "User", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" User state of record ID:"+str(user_obj.id)+" From Status = "+ str(user_obj.is_active)+"  To User Status = "+old_state, generated_by= user)
								user_obj.is_active = True
								
								
								notification.save()
								user_obj.save()
	 
								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/users')
						else:						 
							messages.info(req, "Pease correct Data", extra_tags = "wrong_pass")
							return HttpResponseRedirect('/set-up/users')


					except User.DoesNotExist: 
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_data")
						return HttpResponseRedirect('/set-up/users')
				else:					 
					messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/users')

					 

		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/users')

	else:
		return render(req, 'login.html')

def toggle_office_state(req):
	 
	user_access_level  = req.session.get("access_level")
	
	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == "Super Administrator": 

			if req.method == "GET":				 			
				return HttpResponseRedirect('/set-up/offices')

			elif req.method == "POST" and req.POST:

				form = PasswordTextForm(req.POST)
				if form.is_valid():
					office_id = req.POST.get("office_id")				 
					paswd = form.cleaned_data.get("password") 
	 
					try:

						user_id = req.session['user_id']
						user = User.objects.get(id = user_id)



						if user.password == crypt(paswd, user.password):

							office_obj = Office.objects.get(id = office_id)

							if office_obj.is_active:

								old_state = "Active"
								 
								notification = Notification(notification_for= "Office", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Office state of record ID:"+str(office_obj.id)+" From Status = "+ str(office_obj.is_active)+"  To Charge Status = "+old_state, generated_by= user)
								
								office_obj.is_active = False
								
								notification.save()
								office_obj.save()


								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/offices')

							else:
								
								old_state = "Inactive"
								 
								notification = Notification(notification_for= "Charge", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Office state of record ID:"+str(office_obj.id)+" From Status = "+ str(office_obj.is_active)+"  To Charge Status = "+old_state, generated_by= user)
								office_obj.is_active = True

								notification.save()
								office_obj.save()
	 
								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/offices')
								


						else:
							 
							messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
							return HttpResponseRedirect('/set-up/offices')

					except User.DoesNotExist: 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/login')

					 

		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/offices')

	else:
		return render(req, 'login.html')
def toggle_institution_cat_state(req):
	 
	user_access_level  = req.session.get("access_level")
	
	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == "Super Administrator": 

			if req.method == "GET":				 			
				return HttpResponseRedirect('/set-up/institution-categories/')

			elif req.method == "POST" and req.POST:

				form = PasswordTextForm(req.POST)
				if form.is_valid():
					category_id = req.POST.get("category_id")				 
					paswd = form.cleaned_data.get("password") 
	 
					try:

						user_id = req.session['user_id']
						user = User.objects.get(id = user_id)



						if user.password == crypt(paswd, user.password):

							print(category_id)

							institution_obj = InstitutionCategory.objects.get(id = category_id)

							if institution_obj.is_active:
								
								old_state = "Active"
								 
								notification = Notification(notification_for= "Institution", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Office state of record ID:"+str(institution_obj.id)+" From Status = "+ str(institution_obj.is_active)+"  To Institution Category Status = "+old_state, generated_by= user)
								institution_obj.is_active = False
								notification.save()
								institution_obj.save()


								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/institution-categories')

							else:
								
								old_state = "Inactive"
								 
								notification = Notification(notification_for= "Institution", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Office state of record ID:"+str(institution_obj.id)+" From Status = "+ str(institution_obj.is_active)+"  To Institution Category Status = "+old_state, generated_by= user)
								
								institution_obj.is_active = True
								notification.save()
								institution_obj.save()
	 
								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/institution-categories')
								


						else:							 
							messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
							return HttpResponseRedirect('/set-up/institution-categories')

					except User.DoesNotExist: 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/login')
				else:							 
					messages.info(req, "Pease correct Password", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/institution-categories')
					 

		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/institution-categories')

	else:
		return render(req, 'login.html')

def toggle_institution_type_state(req):


	 
	user_access_level  = req.session.get("access_level")
	
	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == "Super Administrator": 

			if req.method == "GET":				 			
				return HttpResponseRedirect('/set-up/institution-types/')

			elif req.method == "POST" and req.POST:

				form = PasswordTextForm(req.POST)
				if form.is_valid():
					category_id = req.POST.get("category_id")				 
					paswd = form.cleaned_data.get("password") 
	 
					try:

						user_id = req.session['user_id']
						user = User.objects.get(id = user_id)



						if user.password == crypt(paswd, user.password):

							 

							institution_obj = InstitutionType.objects.get(id = category_id)

							if institution_obj.is_active:
								
								old_state = "Active"
								 
								notification = Notification(notification_for= "Institution", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Office state of record ID:"+str(institution_obj.id)+" From Status = "+ str(institution_obj.is_active)+"  To Institution Category Status = "+old_state, generated_by= user)
								institution_obj.is_active = False
								notification.save()
								institution_obj.save()


								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/institution-types')

							else:
								
								old_state = "Inactive"
								 
								notification = Notification(notification_for= "Institution", notification_type = "StatusChange", notification_txt = "User with ID:"+str(user.id)+" Office state of record ID:"+str(institution_obj.id)+" From Status = "+ str(institution_obj.is_active)+"  To Institution Category Status = "+old_state, generated_by= user)
								institution_obj.is_active = True
								notification.save()
								institution_obj.save()
	 
								messages.info(req, "record updated", extra_tags = "record_updated")
								return HttpResponseRedirect('/set-up/institution-types')
								


						else:							 
							messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
							return HttpResponseRedirect('/set-up/institution-types')

					except User.DoesNotExist: 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/login')
				else:							 
					messages.info(req, "Pease correct Password", extra_tags = "wrong_data")
					return HttpResponseRedirect('/set-up/institution-types')
					 

		else:
			messages.info(req, "Access Denied", extra_tags = "access_denied")
			return HttpResponseRedirect('/set-up/institution-types')

	else:
		return render(req, 'login.html')
def search_record(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Super Administrator":		 

			if req.method == "GET":
				return render(req, "search_results.html", {"msg":"Please type in a correct tin in a search field to search for a record"})	

			elif req.method == "POST" and req.POST:

				try:
					search_text = req.POST.get("search_text")
					tin_record_obj = AssignedTin.objects.filter(tin = search_text)

					if tin_record_obj.exists():

						existing_tin = tin_record_obj.first()
						if existing_tin.tin_for == "Company":
							 

							company_obj = Company.objects.filter(tin = existing_tin.id)
							return render(req, "search_results.html", {"search_results":company_obj, "for":"company"})

						else:
							 
							individual_obj = Individual.objects.filter(tin = existing_tin.id)
							 
							return render(req, "search_results.html", {"search_results":individual_obj, "for":"individual"})

					else:
						print("no records atteched to this tin")
						return render(req, "search_results.html", {"msg":"No records found "})

						

					 
				except Exception as e:
					print (e)
					return render(req, "search_results.html")	
						
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


def notification_viewed(req, notification_id):
    if req.is_ajax():
        message = "This is ajax"
        try:
        	notification_obj =  Notification.objects.get(id = notification_id)
        	notification_obj.is_viewed = True

        	notification_obj.save()

        	return JsonResponse(True, safe=False)
        except Notification.DoesNotExist:
        	return JsonResponse(True, safe=False)
       
    else:
    	return JsonResponse(False, safe=False)

def logout(req): 

	if ('user_id' in req.session) and ('access_level' in req.session):

		user = User.objects.get(id = req.session['user_id'])
		user.is_onLine = False

		del req.session['user_id']
		del req.session['access_level']

		user.save()
		return render(req, 'login.html')
	# user is still logged in

		
	else:
		return render(req, 'login.html')

		



def edit_lga(req):
	

	if 'user_id' in req.session  and ('access_level' in req.session):		
 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/set-up/lgas')

		elif req.method == "POST" and req.POST:				 
			form = EditLGAForm(req.POST)

						

			if form.is_valid():

				paswd = form.cleaned_data.get("password")
				lga_name = form.cleaned_data.get("lga_name")
				lga_code = form.cleaned_data.get("lga_code")
				office_id = req.POST.get("office_id")

				 
				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):

						lga_obj = LocalGovArea.objects.get(id = office_id)

						notification = Notification(notification_for= "LGA", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+" edited State Code record ID:"+str(lga_obj.id)+" From LGA Name = "+ lga_obj.local_government_name+" , LGA code = "+lga_obj.local_government_code+" To LGA name = "+lga_name+" , LGA code = "+lga_code, generated_by= user)
						

						lga_obj.local_government_name = lga_name
						lga_obj.local_government_code = lga_code

						
						notification.save()
						lga_obj.save()

						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/set-up/lgas')


					else:
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/set-up/lgas')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/set-up/login')
			else:
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/set-up/lgas')


def data_backup(req):
	if req.method =="POST" and req.method:
		clean_old_data = req.POST.get("clean_old_data")
		paswd = req.POST.get("password")

		if clean_old_data == "T":
			clean_old_data = "--clean"
		else:
			clean_old_data = ""
			
		try:
			user_id = req.session['user_id']
			user = User.objects.get(id = user_id)
			
			if user.password == crypt(paswd, user.password):
				
				os.system("python3 manage.py dbbackup --noinput -q --traceback --compress " +clean_old_data)
				notification = Notification(notification_for= "Data", notification_type = "Data Backup", notification_txt = "User with ID:"+str(user.id)+"backup up data" ,generated_by= user)						 						
				notification.save()
				return JsonResponse({"res":"Data Backed Up Sucessfully"})
				
			else:
				 				 
				return JsonResponse({"res":"wrong_pass"})	

	
		except Exception as e:

			return JsonResponse({"res":"Some Thing Wrong Happened"})

def data_restore(req):
	if req.method =="POST" and req.method:
		paswd = req.POST.get("password")
		 
		try:

			user_id = req.session['user_id']
			user = User.objects.get(id = user_id)

			if user.password == crypt(paswd, user.password):

				os.system("python3 manage.py dbrestore --noinput -q --traceback --uncompress")
				notification = Notification(notification_for= "Data", notification_type = "Data Restore", notification_txt = "User with ID:"+str(user.id)+"restored data" , generated_by= user)						 						
				notification.save()
				return JsonResponse({"res":"Data Restored Sucessfully"})
				
			else:						 
				return JsonResponse({"res":"wrong_pass"})
			 
		except Exception as e:
			return JsonResponse({"res":"Some Thing Wrong Happened"})

def media_data_restore(req):
	if req.method =="POST" and req.method:
		paswd = req.POST.get("password")
		 
			
		try:

			user_id = req.session['user_id']
			user = User.objects.get(id = user_id)
			 

			if user.password == crypt(paswd, user.password):

				os.system("python3 manage.py mediarestore --noinput -q --traceback  --uncompress")
				notification = Notification(notification_for= "Data", notification_type = "media Data Restore", notification_txt = "User with ID:"+str(user.id)+"restored media data" , generated_by= user)						 						
				notification.save()
				return JsonResponse({"res":"Media Data Restored Sucessfully"})				
			else:						 
				return JsonResponse({"res":"wrong_pass"})

 
		except Exception as e:
			print(e)
			return JsonResponse({"res":"Some thing Wrong Happened"})


def media_data_backup(req):
	if req.method =="POST" and req.method:
		paswd = req.POST.get("password")
		clean_old_data = req.POST.get("clean_old_data")
		

		if clean_old_data == "T":
			clean_old_data = "--clean"
		else:
			clean_old_data = ""
			
		try:
			user_id = req.session['user_id']
			user = User.objects.get(id = user_id)
			 


			if user.password == crypt(paswd, user.password):

				os.system("python3 manage.py mediabackup --noinput -q --traceback --compress " +clean_old_data)

				notification = Notification(notification_for= "Data", notification_type = "media Data backup", notification_txt = "User with ID:"+str(user.id)+"restored media data" , generated_by= user)						 						
				notification.save()
				return JsonResponse({"res":"Media Data Backed Up Sucessfully"})				
			else:						 
				return JsonResponse({"res":"wrong_pass"})

 
		except Exception as e:
			return JsonResponse({"res":"Some Thing went wrong"})

def data_management(req):	 
 		return render(req, 'data_management.html')