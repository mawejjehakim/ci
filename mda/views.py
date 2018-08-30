from django.shortcuts import render

from django.core.mail import send_mail

from mda.forms import MDAForm, TINForm, MDAEbillForm, BillForm
from mda.models import MDA, RevenueItem,  MDAEbill

from tin.models import AssignedTin, Company, Individual

from django.http import HttpResponseRedirect

from django.contrib import messages


from random import randint


	 
 

def t_code():
	range_start = 10**(8-1)
	range_end = (10**8)-1
	generated_rand_num =  randint(range_start, range_end)
	tcode = "BRN"+str(generated_rand_num)

	return tcode

def mdas(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'MLA Administrator' or 'Super Administrator':			 
			mdas = MDA.objects.all()
			
			return render(req, 'mdas.html', {"mdas":mdas})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')


def add_mda(req):

 
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA Administrator' or "Super Administrator":		 

			if req.method == "GET":
								
				return render(req, 'add_mda.html')

			elif req.method == "POST" and req.POST:				 
				form = MDAForm(req.POST)

				if form.is_valid():
				
					try:

						mda_name = form.cleaned_data.get("mda_name")
						
						mda_obj, created =  MDA.objects.get_or_create(mda_name = mda_name, aprvd_18 = 33)

						if created:
							 

							messages.success(req, "MDA Created", extra_tags = "mda_created")
							return HttpResponseRedirect('/mda/add-mda/')

						else:	
							 			 
							messages.success(req, "MDA already exist", extra_tags = "record_already_exist")
							return HttpResponseRedirect('/mda/add-mda/')

					except Exception as e:	
						print(e)		 
						messages.info(req, "uncaught Exception")
						return HttpResponseRedirect('/mda/add-mda/')	
					
				else:
					print(form.errors)
					messages.info(req, "invalid form fields")
					return HttpResponseRedirect('/mda/add-mda/')
				
			else:
				messages.success(req, "add mda")
				return render(req, 'add_mda.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')


# **********************
	

def get_tin_info_generate_bill(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA Administrator' or "Super Administrator":

			if req.method == "GET":
				return render(req, 'get_tin_info_generate_bill.html')			

			elif req.method == "POST" and req.POST: 		 
				form = TINForm(req.POST)

				if form.is_valid():
				
					try:
						tin = form.cleaned_data.get("tin_number")

						tin_obj = AssignedTin.objects.get(tin = tin)
						
						individual_obj = Individual.objects.get(tin = tin_obj.id)

						mdas = MDA.objects.all()

						 
						return  render(req, 'generate_bill.html', {'tin':tin,  "mdas":mdas })


					except AssignedTin.DoesNotExist:
						 
						messages.info(req, "TIN DoesnotExis", extra_tags = "wrong_tin")	
						return  render(req, 'get_tin_info_generate_bill.html')	

					except Individual.DoesNotExist:
						mdas = MDA.objects.all()
						company_obj = Company.objects.get(tin = tin_obj.id)
			 

						return  render(req, 'generate_bill.html', {"tin_for":"company",  "mdas":mdas, 'tin':tin })


					except Company.DoesNotExist:
						messages.info(req, "TIN DoesnotExis", extra_tags = "wrong_tin")	
						return  render(req, 'get_tin_info_generate_bill.html')	

						 


					except Exception as e:			 
						print(e)
						return render(req, 'get_tin_info_generate_bill.html')	
					
				else:
					messages.info(req, "invalid form fields")
					return render(req, 'get_tin_info_generate_bill.html')	

				
			else:				
				return render(req, 'get_tin_info_generate_bill.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		messages.info(req, "sign in")		 
		return render(req, 'login.html')
		 
	

def revenue_items(req):

	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):

		if user_access_level == 'MLA Administrator' or 'Super Administrator':			 
			revenue_items = RevenueItem.objects.all()
			
			return render(req, 'revenue_items.html', {"revenue_items":revenue_items})				
			 
		else:			 
			messages.info(req, "You dont have the right to perform this operation")
			return HttpResponseRedirect('/login/')
		
	else:
		messages.info(req, "Sign in Please")
		return HttpResponseRedirect('/login/')

def add_revenue_item(req):
	user_access_level  = req.session.get("access_level")

	if 'user_id' in req.session  and ('access_level' in req.session):		

		if user_access_level == 'MLA Administrator' or "Super Administrator":		 

			if req.method == "GET":
								
				return render(req, 'add_revenue_item.html')

			elif req.method == "POST" and req.POST:				 
				form = MDAForm(req.POST)

				if form.is_valid():
				
					try:

						mda_name = form.cleaned_data.get("mda_name")
					 
						
						revenue_obj, created =  RevenueItem.objects.get_or_create(mda_name = mda_name)

						if created:
							 

							messages.success(req, "MDA Created", extra_tags = "mda_created")
							return HttpResponseRedirect('/mda/add-revenue-item/')

						else:	
							 			 
							messages.success(req, "MDA already exist", extra_tags = "record_already_exist")
							return HttpResponseRedirect('/mda/add-revenue-item/')

					except Exception as e:	
						print(e)		 
						messages.success(req, "Wrong Data", extra_tags = "wrong_data") 
						return HttpResponseRedirect('/mda/add-revenue-item/')	
					
				else:
					messages.success(req, "Wrong Data", extra_tags = "wrong_data") 
					return HttpResponseRedirect('/mda/add-revenue-item/')
				
			else:
				 
				return render(req, 'add_revenue_item.html')			 

		else:
			# user has no rigth to do this operation 
			messages.info(req, "You dont have the right to perform this operation")			 
			# return render(req, 'login.html')
		
	else:
		 	 
		return render(req, 'login.html')
 

def get_bill(req):
	

	form = MDAEbillForm(req.POST)

	if form.is_valid():
		tcode = t_code()

		tin = form.cleaned_data.get("tin")
		mda_id =form.cleaned_data.get("mda") 
		revenue_item = form.cleaned_data.get("revenue_item")
		period = form.cleaned_data.get("period")
		amount =form.cleaned_data.get("amount") 


		try:
			tin_obj = AssignedTin.objects.get(tin = tin)

			mda_obj = MDA.objects.get(id = mda_id)

			MDAEbill.objects.create(reference_number = tcode, tin = tin_obj, mda = mda_obj , revenue_item = revenue_item, period = period, amount = amount)

			mdaEbill = MDAEbill.objects.filter(reference_number = tcode, tin = tin_obj.id )

			return render(req, 'bill.html', {'tcode':tcode, 'tin':tin_obj.tin, 'mda':mda_obj.mda_name, 'revenue_item':revenue_item, 'period':period, 'amount':amount, 'mda_ebills':mdaEbill})
		
		except AssignedTin.DoesNotExist as e:
			messages.info(req, "tin does not exist", extra_tags = 'wrong_tin')
			return  render(req, 'generate_bill.html')

		except MDA.DoesNotExist as e:
			messages.info(req, "MDA is wrong")
			return  render(req, 'generate_bill.html')
	else:
		messages.info(req, "tin does not exist", extra_tags = 'wrong_data')
		return render(req, "generate_bill.html" )

 

def select_payement(req, tin_number, bill_number):

	tin = tin_number
	bill_no = bill_number

	try:
		
	

		tin_obj = 	AssignedTin.objects.get(tin = tin)
		 
		mba_ebill =  MDAEbill.objects.filter(reference_number = bill_no, tin = tin_obj.id )

		if mba_ebill.exists():
			 
			return render(req, 'select_payement.html', {'tin':tin, 'bill_no':bill_no})


		else:
			 

			return render(req, 'select_payement.html')

	except AssignedTin.DoesNotExist:
		return render(req, 'select_payement.html')
			

 
def select_payement_without_details(req):
	return render(req, 'select_payement.html')

		

	


def make_payement(req):

	form = BillForm(req.POST)

	if form.is_valid():


		bill_no = req.POST.get("bill_no")
		tin = req.POST.get("tin")
		bill_no = req.POST.get("bill_no")
		phone = req.POST.get("phone")
		email = req.POST.get("email")

		try:
			tin_obj = AssignedTin.objects.get(tin = tin)
		
			mba_ebill =  MDAEbill.objects.filter(reference_number = bill_no, tin = tin_obj.id )

			if mba_ebill.exists():
				# send email 
				# /print recept

				if mba_ebill[0].is_paid:
					messages.info(req, "payement success", extra_tags = "payement_already_made")
					return render(req, 'select_payement.html', {'tin':tin, 'bill_no':bill_no})

				else:
					 
				
					mba_ebill.update(is_paid = True)
					send_mail('CoreIGR @ Payement successfull', 'Hello  payement with '+ bill_no +' bill number has been successfull.', 'coreIGR@gmail.com',[email],  fail_silently=False, )
				
					


					messages.info(req, "success ", extra_tags = "payement_successfull")
					return render(req, 'select_payement.html', {'email':email})
				
				

			else:
				messages.info(req, "invalid  form", extra_tags = "invalid_mda_bill")
				return render(req, 'select_payement.html')

		except AssignedTin.DoesNotExist:
			messages.info(req, "invalid  form", extra_tags = "invalid_mda_bill")
			return render(req, 'select_payement.html')
			

	else:
		messages.info(req, "invalid  form", extra_tags = "invalid_form_data")
		return render(req, 'select_payement.html')

	 