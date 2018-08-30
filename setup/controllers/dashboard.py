from django.shortcuts import render
from setup.models import User, Notification
from tin.models import Individual, Company, AssignedTin
from mla.models import Vehicle
from store.models import NumberPlate


from mda.models import MDAEbill

def dashboard(req):
	all_users_count = User.objects.all().count()
	all_individuals_count = Individual.objects.all().count()
	all_vehicles_count = Vehicle.objects.all().count()
	all_companies_count = Company.objects.all().count()
	onLineUsers =  User.objects.filter(is_onLine = True).count()
	offLineUsers = User.objects.filter(is_onLine = False).count()
	individuals_tins_count = AssignedTin.objects.filter(tin_for  = "Individual").count()
	companies_tins_count = AssignedTin.objects.filter(tin_for = "Company").count()

	issued_number_plates_count = NumberPlate.objects.filter(is_issued = True).count()
	taken_number_plates_count = NumberPlate.objects.filter(is_taken = True).count()
	notifications = Notification.objects.filter(is_viewed = False)
	return render(req, 'dashboard.html', {'all_users_count':all_users_count, 'onLineUsers':onLineUsers, 'notifications':notifications, 'issued_number_plates_count':issued_number_plates_count, 'taken_number_plates_count':taken_number_plates_count, 'companies_tins_count':companies_tins_count, "individuals_tins_count":individuals_tins_count, 'offLineUsers':offLineUsers, 'all_individuals_count':all_individuals_count, 'all_vehicles_count':all_vehicles_count, 'all_companies_count':all_companies_count})


 
 



 
