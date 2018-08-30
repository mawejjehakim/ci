from django.db import models
  
from tin import models as tin_models
from setup import models as setup_models

# Create your models here.

class AssignedTin(models.Model):
	TIN_FOR = (	("Individual", "Individual"),	("Company", "Company")	)
	registration_date = models.DateField(auto_now_add=True)
	tin = models.CharField(max_length = 10)
	
	tin_for = models.CharField(max_length = 15, choices = TIN_FOR)


	
class Individual(models.Model):

	GENDER = (
		("Male", "Male"),
		("Female", "Female")
		)
	MARITAL_STATUS = (
		("Married", "Married"),
		("Single", "Single"),
		("Divorced", "Divorced"),
		("Others", "Others")
		)
	registration_date = models.DateField(auto_now_add=True)
	tin = models.ForeignKey(tin_models.AssignedTin, on_delete=models.CASCADE)
	name = models.CharField(max_length = 50 ,null = False)
	gender = models.CharField(max_length = 10, choices = GENDER)
	date_of_birth = models.CharField(max_length = 20)
	marital_status = models.CharField(max_length = 15, choices = MARITAL_STATUS)
	state = models.CharField(max_length = 50)
	address = models.CharField(max_length = 250, null = False)
	phone = models.CharField(max_length = 15, null = False, unique = True)
	email = models.CharField(max_length = 100, unique = True)
	occupation = models.CharField(max_length = 50 ,null = False)
	employment_status = models.CharField(max_length = 15 ,null = False)
	work_place = models.CharField(max_length = 250)
	passport_pic_url = models.CharField(max_length = 150)
	staff = models.ForeignKey(setup_models.User, on_delete = models.CASCADE)
	
class Company(models.Model):

	  registration_date = models.DateField(auto_now_add=True)
	  local_government = models.CharField(max_length = 50)
	  ward = models.CharField(max_length = 50)
	  bussiness_area = models.CharField(max_length = 5)
	  institution = models.CharField(max_length = 50)
	  institution_type =  models.ForeignKey(setup_models.InstitutionType, on_delete=models.CASCADE)
	  institution_category =  models.ForeignKey(setup_models.InstitutionCategory, on_delete=models.CASCADE)
	  bussiness_status = models.CharField(max_length = 50)
	  bussiness_class = models.CharField(max_length = 50)
	  registration_number = models.CharField(max_length = 20)
	  bussiness_ownership_type = models.CharField(max_length = 50)
	  tin = models.ForeignKey(tin_models.AssignedTin, on_delete=models.CASCADE)
	  jtb_tin = models.CharField(max_length = 10)
	  bussiness_name = models.CharField(max_length = 250)
	  bussiness_owner = models.CharField(max_length = 100)
	  bussiness_address = models.CharField(max_length = 100)
	  phone_number = models.CharField(max_length = 15)
	  email = models.CharField(max_length = 100)
	  bussiness_size = models.CharField(max_length = 50)
	  longtitude = models.CharField(max_length = 10)    
	  latitude = models.CharField(max_length = 10)
	  enumerator = models.CharField(max_length = 50)
	  supervisor = models.CharField(max_length = 50)
	  coordinator = models.CharField(max_length = 50)
	  staff = models.ForeignKey(setup_models.User, on_delete=models.CASCADE, null = False)
	 