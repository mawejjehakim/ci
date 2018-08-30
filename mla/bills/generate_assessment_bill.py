from mla.bills.bills.bill_ps import bill_ps 
from mla.bills.bills.bill_cvs import bill_cvs
from mla.bills.bills.bill_ppb import bill_ppb
from mla.bills.bills.bill_dv import bill_dv
from mla.bills.bills.bill_ct import bill_ct
from mla.bills.bills.bill_tm import bill_tm
from mla.bills.bills.bill_pm import bill_pm
from mla.bills.bills.bill_dtm import bill_dtm
from mla.bills.bills.bill_cpb import bill_cpb


def generate_assessment_bill(vehicle_category, tin_obj, engine_size, cost_price, chassis_number, staff_obj):
	print(vehicle_category)


	if vehicle_category == "Private Vehicle Saloon":
		 
		return bill_ps(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Vehicle Saloon":
		return bill_cvs(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Private Pickup/Bus":
		return bill_ppb(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Pickup/Bus":
		return bill_cpb(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Dealers Vehicle":
		return bill_dv(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
		return bill_ct(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Tricycle/Motorcycle":
		return bill_tm(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Private Motorcycle":
		return bill_pm(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
	
	elif vehicle_category == "Dealers Tricycle/Motorcycle":
		return bill_dtm(tin_obj, engine_size, cost_price, chassis_number, staff_obj)
	


# _SESSION['xtcode'] = tcode;
# _SESSION['assessment_chassis'] = chassis;
 