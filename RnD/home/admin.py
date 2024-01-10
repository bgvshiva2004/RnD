from django.contrib import admin
from .models import table_info,project_details
# Register your models here.
admin.site.register(table_info)

@admin.register(project_details)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id','Project_Fellowship_No']
