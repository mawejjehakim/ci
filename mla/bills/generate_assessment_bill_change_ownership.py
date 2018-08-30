
from mla.bills.change_ownership_bills.change_pm import change_pm
from mla.bills.change_ownership_bills.change_ct import change_ct
from mla.bills.change_ownership_bills.change_ps import change_ps
from mla.bills.change_ownership_bills.change_dtm import change_dtm
from mla.bills.change_ownership_bills.change_dv import change_dv
from mla.bills.change_ownership_bills.change_tm import change_tm
from mla.bills.change_ownership_bills.change_cpb import change_cpb
from mla.bills.change_ownership_bills.change_cvs import change_cvs
from mla.bills.change_ownership_bills.change_ppb import change_ppb


def generate_assessment_bill_change_ownership(transaction_code, tin_obj, vehicle_category, engine_size, cost_price, chassis_number, staff_obj):


	if vehicle_category == "Private Vehicle Saloon":
		print("kjhgfd nnnnnnnn")
		return change_ps(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Vehicle Saloon":
		print("kjhgfd nnnnnnnn")
		return change_cvs(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Private Pickup/Bus":
		print("kjhgfd nnnnnnnn")
		return change_ppb(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Pickup/Bus":
		print("kjhgfd nnnnnnnn")
		return change_cpb(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Dealers Vehicle":
		print("kjhgfd nnnnnnnn")
		return change_dv(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Truck/Trailer/Lorry/Tipper":
		return change_ct(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Commercial Tricycle/Motorcycle":
		print("kjhgfd nnnnnnnn")
		return change_tm(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
		
	elif vehicle_category == "Private Motorcycle":
		print("kjhgfd nnnnnnnn")
		return change_pm(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
	
	elif vehicle_category == "Dealers Tricycle/Motorcycle":
		print("kjhgfd nnnnnnnn")
		return change_dtm(transaction_code, tin_obj, engine_size, cost_price, chassis_number, staff_obj)
	

