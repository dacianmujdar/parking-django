from django.contrib import admin

# Register your models here.
import models

admin.site.register(models.Parking)
admin.site.register(models.Request)
admin.site.register(models.RequestType)
