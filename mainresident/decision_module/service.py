import json

from mainresident.decision_module.models import ChallengeResponseEntity
from mainresident.device_manager.models import AuthenticatedDevice
from mainresident.hidden_protocol_interpreter.service import send_icmp_packet




def make_decision_on_alert(alert):
    # match alert to challenge response entity
    # if match, return action
    # else return allow
    print("Alert received")
    entities = ChallengeResponseEntity.objects.all()
    for entity in entities:
        if entity.alert_type == alert.alert_type:
            if match_conditions(entity, alert):
                target_device = AuthenticatedDevice.objects.get(device_ip=alert.device_ip)
                data = {"ip": alert.src_ip, "action": entity.action}
                send_icmp_packet(target_device.device_ip, json.dumps(data))


def match_conditions(entity, alert):
    # match alert to challenge response entity
    # if match, return action
    # else return allow
    if entity.conditions.field_name == "device_id":
        if entity.conditions.value != alert.device_id:
            return False
    elif entity.conditions.field_name == "port":
        if entity.conditions.value != alert.port:
            return False
    elif entity.conditions.field_name == "src_ip":
        if entity.conditions.value != alert.src_ip:
            return False
    elif entity.conditions.field_name == "dst_ip":
        if entity.conditions.value != alert.dst_ip:
            return False
    return True



