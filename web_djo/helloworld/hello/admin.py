from django.contrib import admin
from hello import models
# Register your models here.
admin.site.register(models.user)
admin.site.register(models.Person)
admin.site.register(models.User_admin)