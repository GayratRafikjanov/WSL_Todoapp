from django.contrib import admin
from .models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_completed', 'created_at')     # Поля для отображения в списке
    search_fields = ('title', 'description')    # Возможность поиска по этим полям
    list_filter = ('is_completed',)    # Фильтрация по статусу завершенности


admin.site.register(Task, TaskAdmin)
