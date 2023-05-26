from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'registered_dttm')

admin.site.register(User, UserAdmin)