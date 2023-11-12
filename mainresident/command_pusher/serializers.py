from rest_framework import serializers


class HDLCommandSerializer(serializers.Serializer):
    ip = serializers.CharField(max_length=50, required=False)
    action = serializers.CharField(max_length=50)
