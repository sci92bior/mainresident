from django.db import models

class ActionTypes(models.TextChoices):
    ALLOW = "allow"
    DENY = "deny"
    REDIRECT = "redirect"

class FieldTypes(models.TextChoices):
    device_id = "device_id"
    port = "port"
    src_ip = "src_ip"
    dst_ip = "dst_ip"

class CRCondition(models.Model):
    field_name = models.CharField(max_length=50, choices=FieldTypes.choices)
    value = models.CharField(max_length=50)


class ChallengeResponseEntity (models.Model):
    alert_type = models.CharField(max_length=50)
    conditions = models.ManyToManyField(CRCondition)
    action = models.CharField(max_length=50, choices=ActionTypes.choices)

class Alert(models.Model):
    alert_type = models.CharField(max_length=50)
    device_id = models.CharField(max_length=50)
    port = models.CharField(max_length=50)
    src_ip = models.CharField(max_length=50)
    dst_ip = models.CharField(max_length=50)
    alert_time = models.DateTimeField(auto_now_add=True)

