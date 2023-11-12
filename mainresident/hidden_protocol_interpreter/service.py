import random
import socket
import struct

from mainresident.device_manager.models import AuthenticatedDevice
from mainresident.hidden_protocol_interpreter.serializers import AlertSerializer


def send_icmp_packet(target_host, data):

    icmp_type = 8  # ICMP Echo Request
    icmp_code = 0
    icmp_checksum = 0
    icmp_id = random.randint(0, 0xFFFF)
    icmp_seq = 1  # Sequence number
    payload = data.encode()

    # Create the ICMP header
    icmp_header = struct.pack('!BBHHH', icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq)

    # Combine the ICMP header and payload
    packet = icmp_header + payload

    # Create a raw socket and send the packet
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.sendto(packet, (target_host, 0))
    sock.close()

# Function to receive ICMP packets with hidden data

def check_if_ip_in_authenticated_addresses(ip_address):
    for device in AuthenticatedDevice.objects.all():
        if device.ip_address == ip_address:
            return True
    return False


def receive_icmp_packet():
    icmp = socket.getprotobyname("icmp")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    while True:
        packet_data, addr = sock.recvfrom(1024)
        if check_if_ip_in_authenticated_addresses(addr[0]):
            icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq = struct.unpack('!BBHHH', packet_data[:8])
            data = packet_data[8:].decode()
            serializer = AlertSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

            print(f"Received ICMP Packet from {addr}: {data}")
        else:
            print(f"{addr} is not in Authenticated addresses. Packet from {addr} dropped")
            break
