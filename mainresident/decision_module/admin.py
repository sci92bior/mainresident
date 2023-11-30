from django.contrib import admin

from mainresident.decision_module.models import Alert, ChallengeResponseEntity, CRCondition


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    readonly_fields = ('alert_type', 'device_ip', 'port', 'src_ip', 'dst_ip', 'alert_time')
    list_display = ('alert_type', 'device_ip', 'port', 'src_ip', 'dst_ip', 'alert_time')
    list_filter = ('alert_type', 'device_ip', 'port', 'src_ip', 'dst_ip', 'alert_time')


@admin.register(ChallengeResponseEntity)
class ChallengeResponseEntityAdmin(admin.ModelAdmin):
    list_display = ('alert_type', 'action')
    list_filter = ('alert_type', 'action')


@admin.register(CRCondition)
class CRConditionAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'value')
    list_filter = ('field_name', 'value')