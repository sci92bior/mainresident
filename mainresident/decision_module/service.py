from mainresident.command_pusher.serializers import HDLCommandSerializer
from mainresident.decision_module.models import ChallengeResponseEntity
from mainresident.device_manager.models import AuthenticatedDevice
from mainresident.hidden_protocol_interpreter.service import send_icmp_packet


class DecisionService:

    def make_decision_on_alert(self, alert):
        # match alert to challenge response entity
        # if match, return action
        # else return allow
        entities = ChallengeResponseEntity.objects.all()
        for entity in entities:
            if entity.alert_type == alert.alert_type:
                if self.match_conditions(entity, alert):
                    target_device = AuthenticatedDevice.objects.get(device_id=alert.device_id)
                    serializer = HDLCommandSerializer()
                    serializer.create(validated_data={"src_ip": alert.src_ip, "dst_ip": alert.dst_ip,
                                                      "in_port": alert.port,
                                                      "action": entity.action})
                    send_icmp_packet(serializer.data, target_device.ip_address)


    def match_conditions(self, entity, alert):
        # match alert to challenge response entity
        # if match, return action
        # else return allow
        for condition in entity.conditions.all():
            if condition.field_name == "device_id":
                if condition.value != alert.device_id:
                    return False
            elif condition.field_name == "port":
                if condition.value != alert.port:
                    return False
            elif condition.field_name == "src_ip":
                if condition.value != alert.src_ip:
                    return False
            elif condition.field_name == "dst_ip":
                if condition.value != alert.dst_ip:
                    return False
        return True



