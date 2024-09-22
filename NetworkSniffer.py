

#importing scapy framework for network analysis
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP  # Explicitly import the layers
# date and time to capture realtime network sessions
import datetime


# Function to process each packet
def packet_callback(packet):
    # Part to Check if the packet has IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Timestamp: {datetime.datetime.now()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

        # Check for TCP or UDP protocols
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP")
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Protocol: UDP")
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")

        print("-" * 40)


# Sniffing packets
def start_sniffer(interface=None):
    print("Starting packet capture...")
    # Start sniffing on specified all interfaces)
    sniff(iface=interface, prn=packet_callback, store=False)


if __name__ == "__main__":
    # "eth0", "wlan0",
    start_sniffer(interface=None)


