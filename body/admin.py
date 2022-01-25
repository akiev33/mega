from django.contrib import admin
from .models import Employee, Employees_in_project


admin.site.register(Employee)
admin.site.register(Employees_in_project)