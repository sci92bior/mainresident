import json
import re
import socket
import struct


def receive_icmp_packet():
    icmp = socket.getprotobyname("icmp")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    while True:
        packet_data, addr = sock.recvfrom(1024)
        icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq = struct.unpack('!BBHHH', packet_data[:8])
        data = packet_data[8:].decode()
        pattern = r'\{.*?\}'

        # Find and extract the content within curly braces
        match = re.search(pattern, data)
        if match:
            json_content = match.group()
            try:
                # Parse the extracted JSON string
                json_data = json.loads(json_content)
                print("Extracted JSON value:", json_data)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")
            print("Extracted JSON content:", json_content)
        else:
            print("No JSON content found in the string.")


if __name__ == '__main__':
    receive_icmp_packet()
