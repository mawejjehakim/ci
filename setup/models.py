from django.db import models

from setup import models as setup_models

class InstitutionCategory(models.Model):
    category_name = models.CharField(unique = True, max_length = 50, null = False)
    is_active = models.BooleanField(default = True)

class InstitutionType(models.Model):
    type_name = models.CharField(unique = True, max_length = 50, null = False)
    is_active = models.BooleanField(default = True)


class Office(models.Model):
  office_name = models.CharField(max_length = 255, unique = True)
  is_active = models.BooleanField(default = True)
 

class User(models.Model):
	"""docstring for ClassName"""
	ACCSESS_LEVEL = (

        ("Super Administrator", "Super Administrator"),
        ("TIN User", "TIN User"),
        ("MLA User", "MLA User"),
        ("MLA Administrator", "MLA Administrator"),
        ("PAYEE User", "PAYEE User"),
        ("DA User", "DA User"),
        ("Store User", "Store User")
		)
	registration_date = models.DateField(auto_now_add=True)
	full_name = models.CharField(max_length = 50, null = False)
	department = models.CharField(max_length = 250, null = False)
	office = models.ForeignKey( Office, on_delete=models.CASCADE)
	user_name = models.CharField(max_length = 50, unique = True, null = False)
	password = models.CharField(max_length = 256,default = "password")
	access_level =  models.CharField(max_length = 50, choices = ACCSESS_LEVEL)
	is_active = models.BooleanField(default = True)
	is_onLine = models.BooleanField(default = False)

    
class Charge(models.Model):
	OPTIONS = (
		("New", "New"),
		("Renew", "Renew")
		)
	options = models.CharField(max_length = 10, null = False, choices = OPTIONS )
	vehicle_type = models.CharField(max_length = 150, null = False)
	particulars	=  models.CharField(max_length = 150)
	amount = models.FloatField(null = False)
	is_active = models.BooleanField(default = True)

class ChargesOthers(models.Model):
    particulars	=  models.CharField(max_length = 150, unique = True)
    amount = models.FloatField(null = False)
    is_active = models.BooleanField(default = True)
 

class LocalGovArea(models.Model):
      local_government_name = models.CharField(unique = True, max_length = 50, null = False)
      local_government_code = models.CharField(unique = True, max_length = 2, null = False)
 

class StateCode(models.Model):
	"""docstring for StatusCode"""
	state_code = models.CharField(max_length = 2, null = False)
	# state_name = models.CharField(max_length = 30, null = False)


class Notification(models.Model):
	"""docstring for StatusCode"""
	registration_date = models.DateField(auto_now_add=True)
	notification_for = models.CharField(max_length = 15, null = False)
	notification_type = models.CharField(max_length = 15, null = False)
	notification_txt = models.CharField(max_length = 705, null = False)
	generated_by = models.ForeignKey(User, on_delete=models.CASCADE, null = False)
	is_viewed = models.BooleanField(default = False)
	 