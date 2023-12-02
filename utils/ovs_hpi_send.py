import socket
import struct
import json
import random

def send_icmp_packet(target_host, port, action):
    icmp_type = 8  # ICMP Echo Request
    icmp_code = 0
    icmp_checksum = 0
    icmp_id = random.randint(0, 0xFFFF)
    icmp_seq = 1  # Sequence number

    # Combine the data and additional_data into a JSON object
    payload_data = json.dumps({"port": port, "action": action}).encode('utf-8')

    # Create the ICMP header
    icmp_header = struct.pack('!BBHHH', icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq)

    # Combine the ICMP header and payload
    packet = icmp_header + payload_data

    # Create a raw socket and send the packet
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    sock.bind(("192.168.3.4", 0))
    sock.sendto(packet, (target_host, 0))
    sock.close()
