from django.db import models


class ActionTypes(models.TextChoices):
    ALLOW = "allow"
    DROP = "drop"


class FieldTypes(models.TextChoices):
    device_id = "device_id"
    port = "port"
    src_ip = "src_ip"
    dst_ip = "dst_ip"


class CRCondition(models.Model):
    field_name = models.CharField(max_length=50, choices=FieldTypes.choices)
    value = models.CharField(max_length=50)

    def __str__(self):
        return self.field_name + " " + self.value


class ChallengeResponseEntity (models.Model):
    alert_type = models.CharField(max_length=50)
    conditions = models.ForeignKey(CRCondition, on_delete=models.CASCADE, blank=True, null=True, related_name="conditions")
    action = models.CharField(max_length=50, choices=ActionTypes.choices)

    def __str__(self):
        return self.alert_type + " " + self.action


class Alert(models.Model):
    alert_type = models.CharField(max_length=50)
    device_id = models.CharField(max_length=50)
    port = models.CharField(max_length=50)
    src_ip = models.CharField(max_length=50)
    dst_ip = models.CharField(max_length=50)
    alert_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alert_type

