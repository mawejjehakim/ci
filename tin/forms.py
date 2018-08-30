from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from tin.models import Company, Individual 
 
class IndividualForm(ModelForm):
	"""docstring for IndivualRegistration"""
	class Meta:
		model = Individual			 
		fields = ('name', 'gender', 'date_of_birth', 'marital_status', 'state', 'address', 'email', 'occupation', 'employment_status','phone' )

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		fields = ('institution', 'bussiness_status', 'bussiness_class','registration_number', 'bussiness_ownership_type', 'bussiness_name', 'bussiness_owner', 'bussiness_address', 'phone_number', 'email' ) 


class EditIndividualForm(forms.Form):
	password = forms.CharField( max_length=30)
	name = forms.CharField(max_length = 50 )
	gender = forms.CharField(max_length = 10 )
	date_of_birth = forms.CharField(max_length = 20)
	marital_status = forms.CharField(max_length = 15)
	state = forms.CharField(max_length = 50)
	address = forms.CharField(max_length = 250 )
	phone = forms.CharField(max_length = 15)
	email = forms.CharField(max_length = 100)
	occupation = forms.CharField(max_length = 50)
	employment_status = forms.CharField(max_length = 15)
	work_place = forms.CharField(max_length = 250)

class EditCompanyForm(forms.Form):
	institution = forms.CharField(max_length = 50)
	bussiness_status = forms.CharField(max_length = 50)
	bussiness_class = forms.CharField(max_length = 50)
	registration_number =forms.CharField(max_length = 30)
	bussiness_ownership_type =forms.CharField(max_length = 50)
	bussiness_name =forms.CharField(max_length = 100)
	bussiness_owner = forms.CharField(max_length = 100)
	bussiness_address = forms.CharField(max_length = 150)
	phone_number = forms.CharField(max_length = 15)
	email = forms.CharField(max_length = 100)	 
	institution_type= forms.CharField(max_length = 50)
	institution_category  = forms.CharField(max_length = 50)
	local_government = forms.CharField(max_length = 100)
	password =  forms.CharField(max_length = 50)
 