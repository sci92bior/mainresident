from django.apps import AppConfig
from django.core.management import call_command


class HPIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainresident.hidden_protocol_interpreter'

    def ready(self):
        # Automatically start listening for messages when the app starts
        call_command('listen_for_messages')