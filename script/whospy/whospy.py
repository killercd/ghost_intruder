import argparse
from scapy.all import sniff, DNS, DNSQR, get_if_list, get_if_addr
import netifaces



def list_interface():
    """
    Lists available network interfaces.
    """
    interfaces = get_if_list()
    print("==============================")
    print("Available network interfaces:")
    print("==============================")
    print("")


    for iface in interfaces:
        ip_address = get_if_addr(iface)
        print(f"{iface}\t{ip_address}")


def log_dns(packet, output_file):
    """
    Logs DNS queries and responses from the packet to the output file.
    """
    if packet.haslayer(DNS):
        dns_layer = packet[DNS]
        if dns_layer.qr == 0:
            query_name = dns_layer[DNSQR].qname.decode('utf-8')
            log_message = f"DNS Query: {query_name}"
        else:
            query_name = dns_layer[DNSQR].qname.decode('utf-8')
            answers = [dns_layer.an[i].rdata for i in range(dns_layer.ancount)]
            answers_str = ", ".join(map(str, answers))
            log_message = f"DNS Response for {query_name}: {answers_str}"
        
        print(log_message)
        if output_file:
            with open(output_file, 'a') as f:
                f.write(log_message + '\n')

def main():
    parser = argparse.ArgumentParser(description="Windows spy detector")
    parser.add_argument("--list-interfaces", required=False, action='store_true', help="List network interfaces")
    parser.add_argument(
        "-i", "--interface",
        default="",
        help="Network interface to sniff on (e.g., Ethernet, Wi-Fi)"
    )
    parser.add_argument(
        "-o", "--output",
        default="dnsdata.txt",
        help="File to save DNS logs (default: None, print to console only)"
    )
    parser.add_argument(
        "-t", "--time",
        default=20,
        help="Sniff data for X seconds"
    )
    

    args = parser.parse_args()

    if args.list_interfaces:
        list_interface()
    else:

        sniff(
            iface=args.interface,
            filter="udp port 53",
            prn=lambda pkt: log_dns(pkt, args.output),
            store=False
        )
    

if __name__=="__main__":
    main()