from django.contrib import admin
from app_users.models import Contact, UserProfileInfo
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(Contact)
