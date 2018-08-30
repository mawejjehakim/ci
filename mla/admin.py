from django.contrib import admin

from mla.models import LearnersPermit, Revalidation, TransactionAssessment
# Register your models here. 
admin.site.register(LearnersPermit)
admin.site.register(Revalidation)
admin.site.register(TransactionAssessment)