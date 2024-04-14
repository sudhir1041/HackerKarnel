from django.contrib import admin
from .models import User,Task
from import_export.admin import ExportActionMixin



admin.site.register(User)

class TaskAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display=[
       'id', 'user_name','task_detail','task_type' 
    ]

    def user_name(self, obj):
        return obj.user.name  
    user_name.short_description = 'User Name'
    
admin.site.register(Task,TaskAdmin)
