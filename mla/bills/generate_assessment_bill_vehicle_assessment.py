
from mla.bills.renew_bills.renew_pm import renew_pm
from mla.bills.renew_bills.renew_ct import renew_ct
from mla.bills.renew_bills.renew_ps import renew_ps
from mla.bills.renew_bills.renew_dtm import renew_dtm
from mla.bills.renew_bills.renew_dv import renew_dv
from mla.bills.renew_bills.renew_tm import renew_tm
from mla.bills.renew_bills.renew_cpb import renew_cpb
from mla.bills.renew_bills.renew_cvs import renew_cvs
from mla.bills.renew_bills.renew_ppb import renew_ppb


def generate_assessment_bill_vehicle_assessment(vehicle_category,  assessment_type, tin_obj, chassis_number, staff_obj):

			 

	if vehicle_category == "Private Vehicle Saloon":
		 
		return renew_ps(assessment_type, tin_obj, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Vehicle Saloon":
		return renew_cvs(assessment_type, tin_obj, chassis_number, staff_obj)
		
	elif vehicle_category == "Private Pickup/Bus":
		return renew_ppb(assessment_type, tin_obj, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Pickup/Bus":
		return renew_cpb(assessment_type, tin_obj, chassis_number, staff_obj)

	elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
		return renew_ct(assessment_type, tin_obj, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Tricycle/Motorcycle":
		return renew_tm(assessment_type, tin_obj, chassis_number, staff_obj)
		
	elif vehicle_category == "Private Motorcycle":
		return renew_pm(assessment_type, tin_obj, chassis_number, staff_obj)

	elif vehicle_category == "Dealers Vehicle":

		return renew_dv(assessment_type, tin_obj, chassis_number, staff_obj)
		
	elif vehicle_category == "Dealers Tricycle/Motorcycle":
		return renew_dtm(assessment_type, tin_obj, chassis_number, staff_obj)
