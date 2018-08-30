from django.forms import ModelForm 
from django import forms
from store.models import NumberPlate


class PlateNumberForm(ModelForm):
	class Meta:
		model = NumberPlate
		fields = ('number_plate', )

 
class EditPlateNumberForm(forms.Form):
	plate_number = forms.CharField( max_length=8)
	
	password = forms.CharField( max_length=30)
