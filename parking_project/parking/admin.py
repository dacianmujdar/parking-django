from django.contrib import admin

from parking_project.parking.models import Parking, Request, RequestType

admin.site.register(Parking)
admin.site.register(Request)
admin.site.register(RequestType)
