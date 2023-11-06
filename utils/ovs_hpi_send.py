import random
import socket
import struct


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

if __name__ == '__main__':
    send_icmp_packet('192.168.4.244',"Hello World!")
