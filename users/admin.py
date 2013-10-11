from django.contrib import admin
from users.models import User

# class UserAdmin(admin.ModelAdmin):
#     fiels = ['firstName', 'lastName', 'email', 'dateOfBirth']

admin.site.register(User)