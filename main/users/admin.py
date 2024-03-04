from django.contrib import admin

from django.contrib.auth.models import User, Group
from django.contrib import admin
from .models import CustomUser

# Unregisters default group and user models from admin site
# admin.site.unregister(Group)
# admin.site.unregister(User)

# Registers customers with admin site
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'phone_number']
    search_fields = ['id', 'user__first_name', 'user__last_name', 'user__email', 'phone_number']
    