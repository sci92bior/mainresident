from rest_framework import serializers

from mainresident.decision_module.models import ActionTypes


class HDLCommandSerializer(serializers.Serializer):
    src_ip = serializers.CharField(max_length=50)
    dst_ip = serializers.CharField(max_length=50)
    in_port = serializers.CharField(max_length=50)
    out_port = serializers.CharField(max_length=50, required=False)
    action = serializers.CharField(max_length=50, choices=ActionTypes.choices)