from django.shortcuts import render
from django.contrib import messages
from store.models import NumberPlate
from setup.models import LocalGovArea, User, Office, Notification
from store.forms import PlateNumberForm, EditPlateNumberForm
from setup.forms import PasswordTextForm
from django.http import JsonResponse
from django.db import IntegrityError
from pbkdf2 import crypt
from django.http import HttpResponseRedirect




def number_plates(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == "Store User" or 'Super Administrator':			 
			number_plates = NumberPlate.objects.all()
			LGAs = LocalGovArea.objects.all()
			
			return render(req, 'number_plates.html', {"number_plates":number_plates, "LGAs":LGAs})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')



def add_number_plate(req):

	user_access_level  = req.session.get("access_level")
	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Store User" or "Super Administrator" :		 

			 
			LGAs = LocalGovArea.objects.all()

			return render(req, 'add_number_plate.html', {"LGAs":LGAs })
	 
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')



def number_plate_record_preview(req):

 
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Store User" or  "Super Administrator":		 

			if req.method == "GET":
						
				return HttpResponseRedirect('/store/add-number-plate/')

			elif req.method == "POST" and req.POST:				 

				form = PlateNumberForm(req.POST)

				if form.is_valid():


					local_government = req.POST.get('local_government')
					number_plate = form.cleaned_data.get("number_plate")
					

					try:			
						office = NumberPlate.objects.get(number_plate = number_plate)		

						messages.success(req, " Record Preview ",  extra_tags = 'plate_exist' )
						return render(req, 'add_number_plate.html')
				 	
 
 


					except NumberPlate.DoesNotExist:

						data_context = {'local_government':local_government, 'number_plate':number_plate, }
						messages.success(req, "Record Preview ",  extra_tags = 'record_preview' )
						return render(req, 'add_number_plate.html', data_context)

					
					except Exception as e:					 
						messages.info(req, "Un Caught Exception")
						return HttpResponseRedirect('/store/add-number-plate/')		
					
				else:
					messages.success(req, "Wrong data ",  extra_tags = 'wrong_data' )					 
					 
					return HttpResponseRedirect('/store/add-number-plate/')
				
			else:
				
				return HttpResponseRedirect('/store/add-number-plate/')				 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')
 



def save_number_plate(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Store User" or  "Super Administrator":	
			

			if req.method == "POST" and req.POST: 		 
				user_id = req.session.get("user_id")		 

				number_plate = req.POST.get("number_plate")
				local_government = req.POST.get("local_government")

				staff_obj = User.objects.get(id = user_id) 

				try:
				 
					 
					NumberPlate.objects.create(local_government = local_government, number_plate = number_plate, staff = staff_obj )
					messages.success(req, "NumberPlate Record Created", extra_tags= "record_created")
					return HttpResponseRedirect('/store/add-number-plate/')
					
				except IntegrityError as e:
					print(e)
					messages.success(req, "NumberPlate Already Created", extra_tags= "plate_has_been_added")
					return HttpResponseRedirect('/store/add-number-plate/')
				 
				
				except Exception as e:
					print(e)				
					return HttpResponseRedirect('/store/add-number-plate/')
				 
				

			else:				
				return render(req, 'add_number_plate.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

 


def get_lg_number_plates(req):	

  
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Store User" or  "Super Administrator":

			if req.method == "GET":

				return HttpResponseRedirect('/store/get-office-plates/')

				 				
			elif req.method == "POST" and req.POST:
				 
				LGAs = LocalGovArea.objects.all()
				lga = req.POST.get("lga")
				office_name = req.POST.get("office_name")
				# req.session['temp_sess_PN_office_name'] = office_name
 
				req.session['temp_sess_LGA'] = lga	 


				try:
				 
					office_obj = Office.objects.get(office_name = office_name)	

					number_plates = NumberPlate.objects.filter(local_government = lga, is_issued=False, is_taken = False)

					issued_number_plates = NumberPlate.objects.filter( office = office_obj.id, is_issued = True)
					req.session['sess_office_id'] = office_obj.id

					return render(req, 'assign_plate_number.html', {"LGAs":LGAs,'number_plates':number_plates,'lg':lga, 'issued_number_plates':issued_number_plates, 'office_name':office_name})
				
				except Office.DoesNotExist as e:
					print(e)
					HttpResponseRedirect('/store/get-office-name/')

				except Exception as e:
					print(e)
					HttpResponseRedirect('/store/get-office-name/')

				# if plate is taken can reas ss
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')






def issue_reissue_number_plate(req):

	
	temp_sess_PN_office_name = req.session['temp_sess_PN_office_name']
	temp_sess_LGA = req.session.get("temp_sess_LGA")
	LGAs = LocalGovArea.objects.all()

	try:
						 
		office_obj = Office.objects.get(office_name = temp_sess_PN_office_name )

		if req.method == "POST" and req.POST:

			plate_number= req.POST.get("plate_number")			 
			number_plate = NumberPlate.objects.get(number_plate = plate_number)



			if (not number_plate.is_issued) and (not number_plate.is_taken):

				#  Assign Plate
				number_plate.office = office_obj
				number_plate.is_issued = True	 
				number_plate.save()

				issued_number_plates = NumberPlate.objects.filter( office = office_obj.id,  is_issued = True)				
				lg_number_plates = NumberPlate.objects.filter(local_government = temp_sess_LGA, is_issued = False, is_taken = False)

				messages.info(req, "Success", extra_tags = "success")

				return render(req, 'assign_plate_number.html', {'office_name':temp_sess_PN_office_name, "LGAs":LGAs, 'number_plates':lg_number_plates,'lg':temp_sess_LGA, "issued_number_plates":issued_number_plates}) 

			elif (number_plate.is_issued) and (not number_plate.is_taken):
				# Re assign Plate

				user_id = req.session['user_id']

				try:
					user = User.objects.get(id = user_id)

					form = PasswordTextForm(req.POST)
					if form.is_valid():	
						paswd = form.cleaned_data.get("password")

						if user.password == crypt(paswd, user.password):
							notification = Notification(notification_for= "Reassign", notification_type = "NumberPlate", notification_txt = "User with ID:"+str(user.id)+" Re-assigned Number Plate:"+str(number_plate.number_plate), generated_by= user)

							number_plate.office = None
							number_plate.is_issued = False	

							notification.save()			 
							number_plate.save()
							
							issued_number_plates = NumberPlate.objects.filter( office = office_obj.id,  is_issued = True)				
							lg_number_plates = NumberPlate.objects.filter(local_government = temp_sess_LGA, is_issued = False, is_taken = False)

							messages.info(req, "Success", extra_tags = "success")
							return render(req, 'assign_plate_number.html', {'office_name':temp_sess_PN_office_name, "LGAs":LGAs, 'number_plates':lg_number_plates,'lg':temp_sess_LGA, "issued_number_plates":issued_number_plates}) 

						else:
							messages.info(req, "Pease correct Data", extra_tags = "wrong_pass")
							return render(req, 'assign_plate_number.html')

					else:											 
						messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
						return render(req, 'assign_plate_number.html')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
					return HttpResponseRedirect('/get-office-plates/')

		else:
			return HttpResponseRedirect('/store/get-office-plates/')

	except NumberPlate.DoesNotExist:
		pass

def get_office_plates(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == "Store User" or  "Super Administrator":

			if req.method == "POST" and req.POST:

				office_name = req.POST.get("office_name")
				LGAs = LocalGovArea.objects.all()
				offices = Office.objects.all()

				 
				 
				req.session['temp_sess_PN_office_name'] = office_name

				office_obj = Office.objects.get(office_name = office_name)
				issued_number_plates = NumberPlate.objects.filter( office = office_obj.id, is_issued = True)

				 
				return render(req, 'assign_plate_number.html', {"office_name":office_name, "LGAs":LGAs,"note_NP_LG":True, "issued_number_plates":issued_number_plates})			

			
			else:
				offices = Office.objects.all() 
				return render(req, 'get_office_name.html', {"offices":offices})	
				
		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')

def edit_number_plate(req):	 
 
	if 'user_id' in req.session  and ('access_level' in req.session): 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/store/plate-numbers/')

		elif req.method == "POST" and req.POST:				 
			form = EditPlateNumberForm(req.POST) 

			if form.is_valid():			 

				plate_id = form.cleaned_data.get("plate_number")				 
				paswd = form.cleaned_data.get("password")

				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):

						
						number_plate_obj = NumberPlate.objects.filter(number_plate = plate_id).delete()

						notification = Notification.objects.create(notification_for= "Number Plate", notification_type = "Delet", notification_txt = "User with ID:"+str(user.id)+	" edited Plate Number PN:"+str(number_plate_obj.number_plate)+" From Plate Number = "+ number_plate_obj.number_plate+", To Plate number = "+plate_number, generated_by= user)
					
					
						
						messages.info(req, "record Deleted", extra_tags = "record_deleted")
						return HttpResponseRedirect('/store/plate-numbers/')
 
					else:						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/store/plate-numbers/')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/store/plate-numbers/')

				 
			else:
				print(form.errors)
			 	 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/store/plate-numbers/')
	else:
		 		 
		return render(req, 'login.html')

def edit_number_plate_lg(req):	 
 
	if 'user_id' in req.session  and ('access_level' in req.session): 	 

		if req.method == "GET":				 			
			return HttpResponseRedirect('/store/plate-numbers/')

		elif req.method == "POST" and req.POST:				 
			form = PasswordTextForm(req.POST) 

			if form.is_valid():
				plate_id = req.POST.get("plate_number_id")				 
				 
				local_government = req.POST.get("local_government")
				paswd = form.cleaned_data.get("password")



				try:
					user_id = req.session['user_id']
					user = User.objects.get(id = user_id)

					if user.password == crypt(paswd, user.password):
						
						number_plate_obj = NumberPlate.objects.get(id = plate_id)

						notification =  Notification(notification_for= "Number Plate", notification_type = "Edit", notification_txt = "User with ID:"+str(user.id)+
							" edited Plate Number PN:"+str(number_plate_obj.number_plate)+" From Local Gov = "+ number_plate_obj.local_government+ ", Local Gov = "+local_government, generated_by= user)
 

						number_plate_obj.local_government = local_government

						notification.save()						
						number_plate_obj.save()
						messages.info(req, "record updated", extra_tags = "record_updated")
						return HttpResponseRedirect('/store/plate-numbers/')
 
					else:
						 
						messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
						return HttpResponseRedirect('/store/plate-numbers/')

				except User.DoesNotExist:
					messages.info(req, "Pease correct Password", extra_tags = "wrong_pass")
					return HttpResponseRedirect('/store/plate-numbers/')

				except IntegrityError as e:
				 
					messages.success(req, "Charge already exist", extra_tags = "record_already_created")
					return HttpResponseRedirect('/store/plate-numbers/')
			else:
			 
				messages.info(req, "Pease correct Data", extra_tags = "wrong_data")
				return HttpResponseRedirect('/store/plate-numbers/')
	else:
		 		 
		return render(req, 'login.html')




def check_number_plate(req, plate_number):
	if req.is_ajax():

		try:
			NumberPlate.objects.get(number_plate  = plate_number)
		 
			return JsonResponse({"res":"taken"})
		except NumberPlate.DoesNotExist:
			 
			return JsonResponse({"res":"not_taken"})
		
		

	else:
		return JsonResponse({"res":"error"})

	 