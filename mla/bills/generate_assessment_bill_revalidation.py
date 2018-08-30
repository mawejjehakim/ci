
from mla.bills.revalidate_bills.revalid_pm import revalid_pm
from mla.bills.revalidate_bills.revalid_ct import revalid_ct
from mla.bills.revalidate_bills.revalid_ps import revalid_ps  
from mla.bills.revalidate_bills.revalid_tm import revalid_tm
from mla.bills.revalidate_bills.revalid_cpb import revalid_cpb
from mla.bills.revalidate_bills.revalid_cvs import revalid_cvs
from mla.bills.revalidate_bills.revalid_ppb import revalid_ppb


def generate_assessment_bill_vehicle_revalidation(vehicle_category, transaction_code,  tin_obj, engine_size, cost_price, chassis_number, staff_obj):
 

	if vehicle_category == "Private Vehicle Saloon":
		print("kkkkkkkkkkkkkkk")
		return revalid_ps(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		 
 
	elif(vehicle_obj.vehicle_category == "Commercial Vehicle Saloon"):
 
		return revalid_cvs(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
				

	elif(vehicle_obj.vehicle_category == "Private Pickup/Bus"):
		return revalid_ppb(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
	

	elif(vehicle_obj.vehicle_category == "Commercial Pickup/Bus"):

		return revalid_cpb(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif(vehicle_obj.vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper"):
		return revalid_ct(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj) 
		
	elif(vehicle_obj.vehicle_category == "Commercial Tricycle/Motorcycle"):
		return revalid_tm(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj) 
		
	elif(vehicle_obj.vehicle_category == "Private Motorcycle"):
		return revalid_pm(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj) 
