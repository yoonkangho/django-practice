from django.contrib import admin

from app.models.user import User, UserAdmin

# Register your models here.
admin.site.register(User, UserAdmin)
