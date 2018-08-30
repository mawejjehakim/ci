from django.db import models
 
from setup import models as setup_models
# Create your models here.

 

class NumberPlate(models.Model):
	"""docstring for NumberPlate"""
	registration_date = models.DateField(auto_now_add=True)
	number_plate  = models.CharField(primary_key =True, max_length = 8) 
	local_government = models.CharField(max_length = 50, null = False)
	office =  models.ForeignKey(setup_models.Office, blank=True, null=True,on_delete=models.SET_NULL )
	staff = models.ForeignKey(setup_models.User, on_delete=models.CASCADE, null = False, related_name = "creator")
	assigned_to_acar_by = models.ForeignKey(setup_models.User, on_delete=models.CASCADE, null=True, related_name="is_issued_by")	
	is_issued = models.BooleanField(default = False)
	is_taken =  models.BooleanField(default = False)


 

        