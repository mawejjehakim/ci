from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from mla.models import Vehicle 
from tin.models import AssignedTin

 

class TinNumberForm(ModelForm):
	class Meta:
		model = AssignedTin
		fields = ('tin', )

class PlateNumberForm(forms.Form):
    number_plate = forms.CharField( max_length=15 )

 

class PlateWithPassForm(forms.Form):
    number_plate = forms.CharField( max_length=15 )
    password = forms.CharField( max_length=30 )

class PlateNumberObjForm(ModelForm):
	class Meta:
		model = Vehicle
		fields =('number_plate',)

class VehicleForm(ModelForm):
	class Meta:
		model = Vehicle
		fields =('chassis_number', 'vehicle_model', 'number_plate', 'vehicle_category', 'gross_weight', 'net_weight', 'no_of_passengers', 'colour',  )
 
class SingleValueCharFieldForm(forms.Form):
	search_text = forms.CharField( max_length=50 ) 

class ChassisNumberFieldForm(forms.Form):
	chassis_number = forms.CharField( max_length=100 ) 
 

class TINForm(forms.Form):
    tin_number = forms.CharField( max_length=10 ) 

class VehicleAssessmentForm(forms.Form):
    search_text = forms.CharField( max_length=30 ) 