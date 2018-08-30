from django.contrib import admin

# Register your models here.
from setup.models import Charge, User, Office, StateCode, InstitutionType, InstitutionCategory, LocalGovArea, ChargesOthers


admin.site.register(Charge)
admin.site.register(User)
admin.site.register(Office)
admin.site.register(StateCode) 
admin.site.register(InstitutionType) 
admin.site.register(InstitutionCategory) 
admin.site.register(LocalGovArea)
admin.site.register(ChargesOthers)