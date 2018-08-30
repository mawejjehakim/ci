from django.db import models

from tin import models as tin_models
from setup import models as setup_models
from store import models as store_models

# Create your models here.

  
class Vehicle(models.Model):
	"""docstring for ClassName"""
	old_owners_tin =  models.CharField(max_length = 10 )
	current_owner_tin = models.ForeignKey(tin_models.AssignedTin, null = False,on_delete=models.CASCADE)
	registration_date = models.DateField(auto_now_add=True)
	chassis_number = models.CharField(unique = True, max_length = 100, null = False)
	vehicle_model = models.CharField(max_length = 100, null = False)
	number_plate =models.ForeignKey(store_models.NumberPlate, null = False, on_delete = models.CASCADE)	 
	vehicle_category = models.CharField(max_length = 50, null = False)
	gross_weight = models.IntegerField(null = False)
	net_weight = models.IntegerField()
	no_of_passengers = models.IntegerField(null = False)
	colour = models.CharField(max_length = 30)
	weight = models.IntegerField()
	engine_size = models.CharField(max_length = 15)
	cost_price = models.CharField(max_length = 50, null = True)
	theft_status = models.BooleanField(default = False)
	staff = models.ForeignKey( setup_models.User, on_delete=models.CASCADE, null = False)
	


class Revalidation(models.Model):
	"""docstring for revalidation"""
	transaction_date = models.DateField(auto_now_add=True)
	tin = models.ForeignKey(tin_models.AssignedTin, on_delete=models.CASCADE, null = False)	
	old_plate_number = models.CharField(max_length = 8, null = False)
	new_plate_number = models.ForeignKey(store_models.NumberPlate, on_delete=models.CASCADE, null = False)
	staff = models.ForeignKey( setup_models.User, on_delete=models.CASCADE, null = False)





class LearnersPermit(models.Model):
 
	is_active = models.BooleanField(default = True)
	transaction_code = models.CharField(max_length = 15, null = False)
	learners_tin =  models.ForeignKey(tin_models.AssignedTin, null = False, on_delete = models.CASCADE)	 
	issue_date = models.DateField( auto_now_add = True)
	expiration_date = models.CharField(max_length = 20)
	particulars = models.CharField(max_length = 150)
	amount = models.FloatField()
	staff = models.ForeignKey( setup_models.User, on_delete=models.CASCADE, null = False)
	 


class TransactionAssessment (models.Model):
  is_expired  = models.BooleanField(default = False )
  transaction_code = models.CharField( max_length = 15, null = False )  
  tin = models.ForeignKey(tin_models.AssignedTin, null = False, on_delete = models.CASCADE)
  chassis_number = models.CharField(max_length = 100, null = False)
  particulars = models.CharField(max_length = 250, null = False)
  amount = models.FloatField(null = False)
  transaction_date =  models.DateField(auto_now_add=True) 
  expiration_date = models.CharField(max_length = 25, null = True)
  transaction_type = models.CharField(max_length = 25)
  payment_status = models.CharField(max_length = 10, default = "Not Paid")  
  staff = models.ForeignKey( setup_models.User, on_delete=models.CASCADE, null = False)
  