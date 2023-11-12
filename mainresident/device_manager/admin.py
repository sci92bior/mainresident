from django.contrib import admin

from mainresident.device_manager.models import AuthenticatedDevice


@admin.register(AuthenticatedDevice)
class AuthenticatedDeviceAdmin(admin.ModelAdmin):
    pass