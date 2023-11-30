import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainresident.decision_module.service import make_decision_on_alert
from mainresident.hidden_protocol_interpreter.serializers import AlertSerializer

logger = logging.getLogger(__name__)

@swagger_auto_schema(methods=['post'], request_body=AlertSerializer)
@api_view(['POST'])
def add_alert(request):
    if request.method == 'POST':
        serializer = AlertSerializer(data=request.data)
        if serializer.is_valid():
            alert = serializer.save()
            logger.warning(f"Alert received. Detected attack type: {alert.alert_type} src ip: {alert.src_ip} dst ip: {alert.dst_ip}")
            make_decision_on_alert(alert)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(request.data)
            print(serializer.errors)
    else:
        return Response("Invalid request method", status=status.HTTP_400_BAD_REQUEST)