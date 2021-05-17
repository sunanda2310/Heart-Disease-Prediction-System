from django.contrib import admin

# Register your models here.

from .models import userInfoModel, userModel

admin.site.register(userInfoModel)
admin.site.register(userModel)
