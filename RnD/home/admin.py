from django.contrib import admin
from .models import project_details
# Register your models here.

@admin.register(project_details)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','Project_Fellowship_No']
