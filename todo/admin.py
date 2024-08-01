from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    #สร้างการเรียงรายการที่หน้า admin
    list_display = ('task', 'is_completed', 'updated_at', 'created_at')
    #สร้าง search สำหรับหน้าแอดมิน
    search_fields = ('task', )

admin.site.register(Task, TaskAdmin)