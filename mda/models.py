from django.db import models
from tin import models as tin_models
from setup import models as setup_models

# Create your models here.


  
class MDAList(models.Model):
  mda_name = models.CharField(max_length = 250, unique = True)




class MDA(models.Model):
  admin_code = models.CharField(max_length = 15)
  mda_name = models.CharField(max_length = 250)
  eco_code = models.CharField(max_length = 15)
  group_title = models.CharField(max_length = 250)
  ipsas_code = models.CharField(max_length = 15)
  ipsas_title = models.CharField(max_length = 250)
  aprvd_18 = models.FloatField(max_length = 50,  null = True)

class RevenueItem(models.Model):
  admin_code = models.CharField(max_length = 15)
  mda_name = models.CharField(max_length = 250)
  eco_code = models.CharField(max_length = 15)
  group_title = models.CharField(max_length = 250)
  ipsas_code = models.CharField(max_length = 15)
  ipsas_title = models.CharField(max_length = 250)
  aprvd_18 = models.FloatField(max_length = 50,  null = True)

class MDAEbill(models.Model):
  transaction_date =  models.DateField(auto_now_add=True)
  reference_number = models.CharField(max_length = 20)
  tin = models.ForeignKey(tin_models.AssignedTin,  on_delete=models.CASCADE)
  
  mda = models.ForeignKey(MDA, on_delete=models.CASCADE)  
  revenue_item = models.CharField(max_length = 250)
  period = models.CharField(max_length = 250)
  amount = models.FloatField()
  is_paid = models.BooleanField(default = False)

class PayeeTaxpayer(models.Model):
  staff_id =  models.ForeignKey(setup_models.User, null = False, on_delete=models.CASCADE)
  staff_name = models.CharField(max_length = 50)
  company_tin =  models.ForeignKey(tin_models.AssignedTin, null = False, on_delete=models.CASCADE)
  company_name = models.CharField(max_length = 250)
  total_gross_income = models.FloatField()
  pension = models.BooleanField(default = False)
  NHIS = models.FloatField()
  NHF = models.BooleanField()
  life_assurance  = models.FloatField()