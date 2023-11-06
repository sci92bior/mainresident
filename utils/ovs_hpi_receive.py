import socket
import struct
import json
import subprocess


def add_ovs_flow(port, action):
    # Define the OVS flow rule based on the received JSON data
    flow_rule = f"priority=100,in_port={port},actions={action}"

    # Use the ovs-vsctl command to add the flow
    cmd = ["ovs-ofctl", "add-flow", "br0", flow_rule]

    try:
        # Execute the ovs-vsctl command
        subprocess.run(cmd, check=True)
        print(f"Added OVS flow for port {port} with action: {action}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add OVS flow: {e}")


def extract_json_from_payload(payload_data):
    try:
        # The JSON-like string starts with "{"
        start_index = payload_data.rfind(b'{')
        if start_index == -1:
            raise ValueError("No JSON-like string found in the payload.")

        # Extract the JSON-like string from the payload
        json_string = payload_data[start_index:]
        json_data = json.loads(json_string.decode('utf-8'))

        return json_data

    except (ValueError, UnicodeDecodeError, json.JSONDecodeError):
        return None

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
            json_data = extract_json_from_payload(payload_data)

            port = json_data.get("port")
            action = json_data.get("action")
            add_ovs_flow(port, action)

            print(f"Received ICMP Packet from {addr}:")
            print(f"Port: {port}")
            print(f"Action: {action}")

        except (UnicodeDecodeError, json.JSONDecodeError):
            # Handle decoding errors or non-JSON data
            print(f"Received ICMP Packet from {addr}: Invalid data")

if __name__ == '__main__':
    receive_icmp_packet()