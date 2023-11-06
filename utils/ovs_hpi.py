import socket
import struct


def receive_icmp_packet():
    icmp = socket.getprotobyname("icmp")
    sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, icmp)

    while True:
        packet_data, addr = sock.recvfrom(1024)
        icmp_type, icmp_code, icmp_checksum, icmp_id, icmp_seq = struct.unpack('!BBHHH', packet_data[:8])
        data = packet_data[8:].split("%")[1]

        try:
            data = data.decode('utf-8')
            print(f"Received ICMP Packet from {addr}: {data}")
        finally:
            print(f"Received ICMP Packet from {addr}: {data}")


if __name__ == '__main__':
    receive_icmp_packet()
