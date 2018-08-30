from django.contrib import admin
from tin.models import AssignedTin, Company, Individual

# Register your models here.


admin.site.register(AssignedTin)
admin.site.register(Company) 
admin.site.register(Individual)