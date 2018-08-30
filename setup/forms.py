from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from setup.models import User, Office, StateCode, LocalGovArea, Charge, ChargesOthers, InstitutionCategory, InstitutionType


 
class LoginForm(ModelForm):
	class Meta:
		model = User
		# fields = ('user_name', 'password')
		fields = ('password',)

class PasswordTextForm(ModelForm):
	class Meta:
		model = User
		# fields = ('user_name', 'password')
		fields = ('password',)







class EditOtherChargeForm(forms.Form):
    amount = forms.FloatField()
    password = forms.CharField( max_length=30) 


class EditOfficeForm(forms.Form):
    office_name = forms.CharField( max_length=150)
    password = forms.CharField( max_length=30) 

class EditLGAForm(forms.Form):
    lga_name = forms.CharField( max_length=60)
    lga_code = forms.CharField( max_length=2)
    password = forms.CharField( max_length=30)


class EditUserForm(forms.Form):
    full_name = forms.CharField( max_length=60)
    user_name = forms.CharField( max_length=80)
    department = forms.CharField( max_length=80)
    access_level = forms.CharField( max_length=80)
    password = forms.CharField( max_length=30)




 

class UserForm(ModelForm):
	class Meta:
		model = User		
		fields = ('full_name', 'department', 'user_name', 'access_level')

class OfficeForm(forms.Form):
    office_name = forms.CharField( max_length=150)

class LocalGovAreaForm(forms.Form):
    local_government_name = forms.CharField( max_length=50)
    local_government_code = forms.CharField( max_length=2)




class EditInstitutionForm(forms.Form):
    institution_text = forms.CharField( max_length=20)
    password = forms.CharField( max_length=30) 

class EditStateCodeForm(forms.Form):
    state_code = forms.CharField( max_length=20)
    password = forms.CharField( max_length=30)


class ChargeForm(ModelForm):
	class Meta:
		model = Charge
		fields =( 'options', 'vehicle_type', 'particulars', 'amount')

class OtherChargeForm(ModelForm):
	class Meta:
		model = ChargesOthers
		fields =( 'particulars', 'amount')

 
 

class InstitutionCategoryForm(ModelForm):
	class Meta:
		model = InstitutionCategory
		fields = ('category_name', )


class InstitutionTypeForm(ModelForm):
	class Meta:
		model = InstitutionType
		fields = ('type_name', )
 

