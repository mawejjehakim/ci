from django.contrib import admin

from mda.models import PayeeTaxpayer, MDAList, MDA, RevenueItem, MDAEbill

admin.site.register(PayeeTaxpayer)
admin.site.register(MDAList)
admin.site.register(MDA)
admin.site.register(RevenueItem) 
admin.site.register(MDAEbill)
# Register your models here.
