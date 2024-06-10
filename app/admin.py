from django.contrib import admin
from .models import Applicant, Customer

# Register your models here.

admin.site.register(Applicant)
admin.site.register(Customer)