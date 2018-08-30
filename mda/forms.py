from django.forms import ModelForm
from django import forms
# from django.contrib.auth.models import User
from mda.models import MDA



 

class MDAForm(ModelForm):
	class Meta:
		model = MDA
		fields = ('mda_name', )


class TINForm(forms.Form):
    tin_number = forms.CharField( max_length=10 ) 

class VehicleAssessmentForm(forms.Form):
    search_text = forms.CharField( max_length=30 ) 

class MDAEbillForm(forms.Form):   

	  tin = forms.CharField(max_length = 10)	   
	  mda = forms.CharField( max_length = 300)  
	  revenue_item = forms.CharField(max_length = 250)
	  period = forms.CharField(max_length = 250)
	  amount = forms.FloatField()

class BillForm(forms.Form):   

	  tin = forms.CharField(max_length = 10)	   
	  bill_no = forms.CharField( max_length = 12)  
	  email = forms.CharField(max_length = 150)
	  phone = forms.CharField(max_length = 15)