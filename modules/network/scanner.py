import ipaddress

from utils.helpers import separator


def port_scanner():
    separator()
    print("BlackShield - IP Information")
    separator()

    ip = input("Enter an IPv4 or IPv6 address: ").strip()

    try:
        addr = ipaddress.ip_address(ip)

        print("\nResults")
        print("-" * 60)
        print(f"IP Address : {addr}")
        print(f"Version    : IPv{addr.version}")
        print(f"Private    : {addr.is_private}")
        print(f"Global     : {addr.is_global}")
        print(f"Loopback   : {addr.is_loopback}")
        print(f"Multicast  : {addr.is_multicast}")
        print(f"Reserved   : {addr.is_reserved}")

    except ValueError:
        print("\nInvalid IP address.")

    separator()
    input("\nPress Enter to continue...")
