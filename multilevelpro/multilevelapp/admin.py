from django.contrib import admin
from .models import Customer, Emp, Student

class AdminStudent(admin.ModelAdmin):
    list_display = ['sname', 'marks']

class AdminCustomer(admin.ModelAdmin):
    list_display = ['cname', 'sales']

class AdminEmp(admin.ModelAdmin):
    list_display = ['ename', 'sal']


admin.site.register(Customer, AdminCustomer)
admin.site.register(Student, AdminStudent)
admin.site.register(Emp, AdminEmp)

# Register your models here.
