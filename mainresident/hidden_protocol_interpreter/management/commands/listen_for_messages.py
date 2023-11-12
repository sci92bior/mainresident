from django.core.management import BaseCommand

from mainresident.hidden_protocol_interpreter.service import receive_icmp_packet


class Command(BaseCommand):
    help = 'Listen for hidden messages'

    def handle(self, *args, **kwargs):
        self.stdout.write('Listening for hidden messages...')
        #receive_icmp_packet()
