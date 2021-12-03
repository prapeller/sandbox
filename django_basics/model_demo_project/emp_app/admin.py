from django.contrib import admin

from emp_app.models import Employee


class EmployeeClassInAdmin(admin.ModelAdmin):
    # pass
    list_display = ['first_name', 'last_name', 'email', 'salary']

admin.site.register(Employee, EmployeeClassInAdmin)
