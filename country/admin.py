from django.contrib import admin

# Register your models here.
from country.models import *
admin.site.register(Country)
admin.site.register(Capital)
