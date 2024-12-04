from django.contrib import admin
from radmin.models import Radmin
# Register your models here.
# admin.site.register(Radmin)
@admin.register(Radmin)

class RAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'description', 'created_at']