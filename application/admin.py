from django.contrib import admin
from .models import Application
# Register your models here.

class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["name", "company", "email", 'phone_number']

admin.site.register(Application, ApplicationAdmin)
