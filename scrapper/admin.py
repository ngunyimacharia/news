from django.contrib import admin

from .models import Country, Provider

# Register your models here.
admin.site.register(Country)
admin.site.register(Provider)
