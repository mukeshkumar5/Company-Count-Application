
from .models import Company
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register the built-in User model
admin.site.unregister(User)
admin.site.register(User, BaseUserAdmin)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "domain", "year_founded", "industry", "size_range", "locality", "country", "linkedin_url", "current_employee_estimate", "total_employee_estimate"]
