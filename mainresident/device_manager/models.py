from django.db import models

class DeviceType (models.TextChoices):
    SWITCH = "switch"
    CONTROLLER = "controller"
    HOST = "host"
    FIREWALL = "firewall"
    IDS = "ids"
    IPS = "ips"
    ROUTER = "router"
    LOAD_BALANCER = "load_balancer"
    VPN_GATEWAY = "vpn_gateway"
    CLOUD = "cloud"
    OTHER = "other"


class AuthenticatedDevice(models.Model):
    device_type = models.CharField(max_length=50, choices=DeviceType.choices, default=DeviceType.OTHER)
    device_id = models.CharField(max_length=50, unique=True)
    device_secret = models.CharField(max_length=50, unique=True)
    device_ip = models.CharField(max_length=50, unique=True)
    hdl_ip = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.device_id + " " + self.device_ip

