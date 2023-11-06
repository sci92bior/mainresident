import socket
import struct
import json


def receive_icmp_packet():
    icmp = socket.getprotobyname("icmp")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    while True:
        packet_data, addr = sock.recvfrom(1024)
        icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq = struct.unpack('!BBHHH', packet_data[:8])
        payload_data = packet_data[8:]
        print(payload_data)

        try:
            # Parse the JSON payload
            json_data = json.loads(payload_data.decode('utf-8'))

            data = json_data.get("data")
            additional_data = json_data.get("additional_data")

            print(f"Received ICMP Packet from {addr}:")
            print(f"Data: {data}")
            print(f"Additional Data: {additional_data}")

        except (UnicodeDecodeError, json.JSONDecodeError):
            # Handle decoding errors or non-JSON data
            print(f"Received ICMP Packet from {addr}: Invalid data")

if __name__ == '__main__':
    receive_icmp_packet()