from django.contrib import admin

from . import models, helper

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('screen_name', 'name', 'description', 'is_active', 'created_at', 'create_time')
    raw_id_fields = ('user',)
    search_fields = ("name", 'screen_name')
    date_hierarchy = 'create_time'
    actions = []


