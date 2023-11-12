from django.urls import path

from mainresident.hidden_protocol_interpreter.views import add_alert

urlpatterns = [
    path('', add_alert, name='add_alert'),
]